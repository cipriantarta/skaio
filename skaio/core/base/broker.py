from abc import ABCMeta, abstractmethod, abstractclassmethod
from typing import Any

from skaio.utils.common import get_loop


class BrokerBase(metaclass=ABCMeta):
    @classmethod
    def create(cls):
        broker = cls()
        broker.loop.run_until_complete(broker.connect())
        return broker

    @property
    def loop(self):
        return get_loop()

    @property
    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def close(self):
        pass

    @abstractmethod
    async def get(self, timeout=0) -> Any:
        pass

    @abstractmethod
    async def put(self, message: Any):
        pass

    @abstractclassmethod
    async def size(self):
        pass

    @property
    def queue(self):
        return 'skaio'

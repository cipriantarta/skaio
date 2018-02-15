from abc import ABCMeta, abstractmethod
from typing import Any

from skaio.core.base.task import BaseTask


class TaskSerializer(metaclass=ABCMeta):

    @abstractmethod
    def serialize(self, task: BaseTask) -> Any:
        pass

    @abstractmethod
    def deserialize(self, data: Any) -> BaseTask:
        pass

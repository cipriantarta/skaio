import abc
from enum import IntEnum, unique


@unique
class Priority(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class BaseTask(metaclass=abc.ABCMeta):
    def __init__(self, priority: Priority=Priority.MEDIUM):
        self.priority = priority

    @abc.abstractmethod
    async def start(self):
        pass

    @abc.abstractmethod
    async def cancel(self):
        pass

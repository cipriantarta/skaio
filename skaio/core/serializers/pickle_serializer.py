import pickle

from skaio.core.base.serializer import TaskSerializer
from skaio.core.base.task import BaseTask


class PickleSerializer(TaskSerializer):

    def serialize(self, task: BaseTask) -> bytes:
        return pickle.dumps(task)

    def deserialize(self, data: bytes) -> BaseTask:
        return pickle.loads(data)

from skaio.core.base.broker import BrokerBase
from skaio.core.base.serializer import TaskSerializer
from skaio.core.brokers.redis import RedisBroker
from skaio.core.serializers.pickle_serializer import PickleSerializer
from skaio.core.base.task import BaseTask


class Publisher:
    def __init__(self, broker: BrokerBase=None, serializer: TaskSerializer=None):
        self.__broker = broker or RedisBroker.create()
        self.__serializer = serializer or PickleSerializer()

    async def publish(self, task: BaseTask):
        await self.__broker.put(self.__serializer.serialize(task))

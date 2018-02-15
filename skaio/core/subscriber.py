from skaio.core.base.broker import BrokerBase
from skaio.core.base.serializer import TaskSerializer
from skaio.core.brokers.redis import RedisBroker
from skaio.core.serializers.pickle_serializer import PickleSerializer


class Subscriber:
    def __init__(self, broker: BrokerBase=None, serializer: TaskSerializer=None):
        self.__broker = broker or RedisBroker.create()
        self.__serializer = serializer or PickleSerializer()

    async def subscribe(self):
        data = await self.__broker.get()
        return self.__serializer.deserialize(data)

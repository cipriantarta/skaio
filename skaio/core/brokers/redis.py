from typing import Dict

from aioredis import create_redis_pool

from skaio.core.base.broker import BrokerBase


class RedisBroker(BrokerBase):
    def __init__(self, host='localhost', db=0, port=6379, max_connections=1000):
        self.host = host
        self.db = db
        self.port = port
        self.max_connections = max_connections
        self.__connection = None

    @property
    def connection(self):
        return self.__connection

    async def connect(self):
        if self.__connection and not self.__connection.closed:
            return self.__connection

        self.__connection = await create_redis_pool(address=(self.host, self.port),
                                                    db=self.db,
                                                    loop=self.loop,
                                                    maxsize=self.max_connections)

    async def close(self):
        if self.connection:
            await self.connection.close()

    async def get(self, timeout=0) -> bytes:
        queue, result = await self.__connection.execute('blpop', self.queue, timeout)
        return result

    async def put(self, data: bytes):
        return await self.__connection.execute('rpush', self.queue, data)

    async def size(self):
        return await self.__connection.execute('llen', self.queue)

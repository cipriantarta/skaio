from skaio.core.base.task import BaseTask


class SimpleTask(BaseTask):
    async def start(self):
        return 'task sample'

    async def cancel(self):
        pass

import importlib.util
import inspect
from skaio import log
from skaio.core.publisher import Publisher
from skaio.core.base.task import BaseTask
from skaio.utils.common import get_loop

tasks = ['samples.simple_tasks']


class Scheduler:
    def start(self):
        publisher = Publisher()
        loop = get_loop()
        for task_mod in tasks:
            m = importlib.import_module(task_mod)
            task_classes = filter(lambda x: inspect.isclass(x[1])
                                  and x[1].__name__ != 'BaseTask'
                                  and issubclass(x[1], BaseTask),
                                  inspect.getmembers(m))

            for name, task in task_classes:
                log.info(f'Sending tasks for {name}')
                loop.run_until_complete(publisher.publish(task))

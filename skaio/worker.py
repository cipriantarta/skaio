import os
from concurrent.futures import ProcessPoolExecutor
from skaio import log

from skaio.core.subscriber import Subscriber
from skaio.utils.common import get_loop


class Worker:
    def __init__(self, max_workers=os.cpu_count()):
        self.max_workers = max_workers

    @classmethod
    def run(cls):
        loop = get_loop()
        worker = Subscriber()

        try:
            while True:
                task = loop.run_until_complete(worker.subscribe())
                log.info(f'[WORKER {os.getpid()}] Received tasks for {task.__name__}')
                instance = task()
                result = loop.run_until_complete(instance.start())
                print(result)
        except Exception as e:
            print(e)

    def start(self):
        log.info(f'Skaio starting with {self.max_workers} workers')
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            for i in range(self.max_workers):
                try:
                    executor.submit(Worker.run)
                except Exception as e:
                    print(e)

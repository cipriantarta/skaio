#!/usr/bin/env python
import asyncio
import argparse
from enum import Enum

import sys

import uvloop

from skaio import log
from skaio.worker import Worker
from skaio.scheduler import Scheduler


class Command(Enum):
    WORKER = 'worker'
    SCHEDULER = 'scheduler'


def main(command: Command):
    if command == Command.WORKER:
        Worker().start()
    elif command == Command.SCHEDULER:
        Scheduler().start()


_help = """
    skaio [command] [options]
"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage=_help, description='asyncio scheduling library')
    parser.add_argument('command', help='Supported commands: worker, scheduler')
    parser.add_argument('--max-workers', help='Number of workers')

    try:
        _ = sys.argv[1]
    except IndexError:
        parser.print_usage()
        exit(1)

    try:
        command = Command[sys.argv[1].upper()]
    except KeyError:
        parser.print_usage()
        exit(1)

    args = parser.parse_args()

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    try:
        main(command)
    except KeyboardInterrupt:
        sys.stderr.write('Shutting down.')

import argparse
import datetime
from todotracker.lib import Command
from todotracker.exceptions import TaskNotFound

from todotracker.db.models import TaskDocument
from todotracker.db.models import WorkDocument, WorkTimeLog

class ListWork(Command):
    COMMAND_NAME = 'list'

    def _init_subparser(self):
        parser = self._parser.add_parser(self.COMMAND_NAME, help='Add Options')

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            workitemlist = WorkDocument.objects
            for workitem in workitemlist:
                print()

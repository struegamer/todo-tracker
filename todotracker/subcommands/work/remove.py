import argparse
import datetime
from todotracker.lib import Command
from todotracker.exceptions import TaskNotFound

from todotracker.db.models import TaskDocument
from todotracker.db.models import WorkDocument, WorkTimeLog

class RemoveWork(Command):
    COMMAND_NAME = 'remove'

    def _init_subparser(self):
        parser = self._parser.add_parser(self.COMMAND_NAME, help='Remove Options')
        parser.add_argument('work_item_id', metavar='WORK_ID', default=None, action='store', help='Task ID')

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            if args.work_item_id is None:
                raise ValueError('WORK_ID can\'t be None')
            try:
                workitem = WorkDocument.objects.get(id=args.work_item_id)
                workitem.delete()
            except Exception as e:
                raise Exception(e)



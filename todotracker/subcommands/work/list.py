import argparse
import datetime
from todotracker.lib import Command
from todotracker.lib import convert_datetime_to_localtime

from todotracker.exceptions import TaskNotFound

from todotracker.db.models import TaskDocument
from todotracker.db.models import WorkDocument, WorkTimeLog

class ListWork(Command):
    COMMAND_NAME = 'list'

    def _init_subparser(self):
        parser = self._parser.add_parser(self.COMMAND_NAME, help='Add Options')

    def _output_header(self):
        print('{0:^30} | {1:^45} | {2:^40}'.format('ID', 'Title', 'Task'))
        print('{0:=<140}'.format(''))
    def _output(self, workitem=None):
        if workitem is None:
            return False
        print('{0:>30} | {1:<45} | {2:<40}'.format(workitem.id, workitem.title, workitem.task.title))
        if len(workitem.timelog) > 0:
            for i in workitem.timelog:
                if i.stop is not None:
                    print('{0:>30} | * {1:>20} / {2:>20} | {3}'.format('',
                                                                 convert_datetime_to_localtime(i.start).strftime('%Y-%m-%d %H:%M:%S'),
                                                                 convert_datetime_to_localtime(i.stop).strftime('%Y-%m-%d %H:%M:%S'), ''))
                else:
                    print('{0:>30} | * {1:>20} / {2:>20} | {3:40}'.format('',
                                                                 convert_datetime_to_localtime(i.start).strftime('%Y-%m-%d %H:%M:%S'),
                                                                 'ongoing', ''))
        return True

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            workitemlist = WorkDocument.objects
            self._output_header()
            for workitem in workitemlist:
                self._output(workitem)

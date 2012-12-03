import os
import argparse

from todotracker.lib import Command
from todotracker.lib import convert_datetime_to_localtime

from todotracker.db.models import TaskDocument
from todotracker.db.models import TagDocument
from todotracker.db.models import WorkDocument, WorkTimeLog


class ShowTask(Command):
    COMMAND_NAME = 'show'

    def _init_subparser(self):
        subparser = self._parser
        parser = subparser.add_parser('show', help='Show Options')
        parser.add_argument('task', metavar='TASK_ID')
        parser.add_argument('details', metavar='DETAILTYPE', choices=['work'], default=None, nargs='?', help='Can be one of the following [work]')

    def _output(self, task):
        title = 'Task: {0}\tProject: {1}'.format(task.title, task.project.title)
        headline = '{0:=<80}'.format('')
        counter = '\tID: {0} (UUID: {1})'.format(task.counter, task.id)
        status = '\tStatus: {0}'.format(task.status)
        created = '\tCreated At: {0}'.format(convert_datetime_to_localtime(task.created_at).strftime('%Y-%m-%d %H:%M:%S'))
        updated = '\tUpdated At: {0}'.format(convert_datetime_to_localtime(task.updated_at).strftime('%Y-%m-%d %H:%M:%S'))
        tags = '\tTags: {0}'.format(', '.join([tag.tag for tag in task.tags]))

        print(title)
        print(headline)
        print(counter)
        print(status)
        print(created)
        print(updated)
        print(tags)

    def _output_todos(self, task):
        title = 'Task: {0}'.format(task.title)
        headline = '{0:=<80}'.format('')
        workitems = '\tTodos:'
        print(title)
        print(headline)
        print(workitems)
        for i in WorkDocument.objects.filter(task=task):
            print i.title
    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can not be None')
        if args.sub_command == self.COMMAND_NAME:
            task = TaskDocument.objects.get(counter=args.task)
            if args.details is None:
                self._output(task)
            if args.details == 'work':
                self._output_todos(task)


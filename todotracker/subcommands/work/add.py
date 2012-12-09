import argparse
import datetime
from todotracker.lib import Command
from todotracker.exceptions import TaskNotFound

from todotracker.db.models import TaskDocument
from todotracker.db.models import WorkDocument, WorkTimeLog

class AddWork(Command):
    COMMAND_NAME = 'add'

    def _init_subparser(self):
        parser = self._parser.add_parser('add', help='Add Options')
        parser.add_argument('task_id', metavar='TASKID', default=None, action='store', help='Task ID')
        parser.add_argument('title', metavar='DESCR', action='store', default='New Work Title', help='Work Item Title')
        parser.add_argument('--start', action='store_true', default=False, help='Start Work after adding', dest='work_start')

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            task = None
            task_id = 0
            if args.task_id is not None:
                try:
                    task_id = int(args.task_id)
                except ValueError as e:
                    raise ValueError('task_id is not a Number')
                try:
                    task = TaskDocument.objects.get(counter=task_id)
                except TaskDocument.DoesNotExist as e:
                    raise TaskNotFound('Task with ID \'{0}\' does not exist'.format(task_id))

                work = WorkDocument()
                work.title = args.title
                work.status = 'new'
                work.task = task
                work.created_at = datetime.datetime.utcnow()
                if args.work_start:
                    timelog = WorkTimeLog()
                    timelog.start = datetime.datetime.utcnow()
                    work.timelog.append(timelog)
                    work.status = 'started'
                work.save()
                print('Workitem \'{0}\' (ID: {1}) added.'.format(work.title, work.id))

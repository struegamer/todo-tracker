import argparse
import datetime

from mongoengine import ValidationError

from todotracker.lib import Command
from todotracker.exceptions import WorkItemNotStarted
from todotracker.exceptions import WorkItemNotFound
from todotracker.exceptions import WorkItemIDNotValid

from todotracker.db.models import TaskDocument
from todotracker.db.models import WorkDocument, WorkTimeLog

class StartWork(Command):
    COMMAND_NAME = 'start'

    def _init_subparser(self):
        parser = self._parser.add_parser(self.COMMAND_NAME, help='Start Options')
        parser.add_argument('work_item_id', metavar='WORK_ID', default=None, action='store', help='Task ID')

    def _check_timelog(self, workitem=None):
        if workitem is None:
            raise ValueError('workitem can\'t be None')
        if len(workitem.timelog) > 0:
            lastitem = workitem.timelog[-1]
            if lastitem.start is not None and lastitem.stop is None:
                raise WorkItemAlreadyStarted('Workitem \'{0}\' (ID: {1}) already started'.format(workitem.title, workitem.id))
        item = WorkTimeLog()
        item.start = datetime.datetime.utcnow()
        workitem.timelog.append(item)
        workitem.save()

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            if args.work_item_id is None:
                raise ValueError('WORK_ID can\'t be None')
            try:
                workitem = WorkDocument.objects.get(id=args.work_item_id)
                self._check_timelog(workitem)
                print('Workitem \'{0}\' (ID: {1} was started'.format(workitem.title, workitem.id))
            except WorkDocument.DoesNotExist:
                raise WorkItemNotFound('Work Item with ID: {0} not found'.format(args.work_item_id))
            except ValidationError:
                raise WorkItemIDNotValid('Not a valid workitem ID: {0}'.format(args.work_item_id))

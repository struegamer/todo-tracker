import argparse
import datetime
from mongoengine import ValidationError
from todotracker.lib import Command
from todotracker.exceptions import WorkItemNotStarted
from todotracker.exceptions import WorkItemNotFound
from todotracker.exceptions import WorkItemIDNotValid

from todotracker.db.models import TaskDocument
from todotracker.db.models import WorkDocument, WorkTimeLog

class StopWork(Command):
    COMMAND_NAME = 'stop'

    def _init_subparser(self):
        parser = self._parser.add_parser(self.COMMAND_NAME, help='Stop Options')
        parser.add_argument('work_item_id', metavar='WORK_ID', default=None, action='store', help='Task ID')

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            if args.work_item_id is None:
                raise ValueError('WORK_ID can\'t be None')
            try:
                workitem = WorkDocument.objects.get(id=args.work_item_id)
                if len(workitem.timelog) > 0:
                    lastitem = workitem.timelog[-1]
                    if lastitem.start is not None and lastitem.stop is None:
                        lastitem.stop = datetime.datetime.utcnow()
                        workitem.timelog[-1] = lastitem
                        workitem.status = 'stopped'
                        workitem.save()
                        print('Work item \'{0} (ID: {1}\' stopped'.format(workitem.title, workitem.id))
                        return
                raise WorkItemNotStarted('Work Item \'{0}\' is not started'.format(workitem.title))
            except WorkDocument.DoesNotExist:
                raise WorkItemNotFound('Work Item with ID: {0} not found'.format(args.work_item_id))
            except ValidationError:
                raise WorkItemIDNotValid('Not a valid workitem ID: {0}'.format(args.work_item_id))





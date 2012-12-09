import os
import argparse
import datetime
from todotracker.lib import Command
import pwd

from todotracker.db.models import TaskDocument
from todotracker.db.models import TagDocument
from todotracker.db.models import ProjectDocument
from todotracker.exceptions import ProjectNotKnown

class AddTask(Command):
    COMMAND_NAME = 'add'

    def __init__(self, parser=None):
        super(AddTask, self).__init__(parser)
        self._username = pwd.getpwuid(os.getuid())[0]

    def _init_subparser(self):
        parser = self._parser.add_parser('add', help='addtask options')
        parser.add_argument('-P', '--project', metavar="PROJ", dest='project', action='store', default=None)
        parser.add_argument('-T', '--tags', metavar='TAGS', dest='tags', action='store', default=None)
        parser.add_argument('tasktitle', metavar='DESCR', default='Empty Title')

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            project = None
            tagdocuments = []
            if args.project is not None and args.project != '':
                # check for Project
                try:
                    project = ProjectDocument.objects.get(title=args.project)
                except ProjectDocument.DoesNotExist as e:
                    raise ProjectNotKnown('{0} is not in the Project List. Add it first'.format(args.project))
            if args.tags is not None and args.tags != '':
                taglist = args.tags.split(',')
                for i in taglist:
                    tagdoc = TagDocument(tag=i).save()
                    tagdocuments.append(tagdoc)
            task = TaskDocument()
            task.title = args.tasktitle
            task.project = project
            task.status = 'new'
            task.created_at = datetime.datetime.utcnow()
            task.updated_at = task.created_at
            task.tags = tagdocuments
            task.user = self._username
            task.save()
            print('Task \'{0}\' (ID: {1}) added'.format(task.title, task.counter))

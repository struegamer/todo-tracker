import argparse
import datetime
from command import Command

from todotracker.db.models import TaskDocument
from todotracker.db.models import TagDocument

class AddTask(Command):
    COMMAND_NAME='addtask'

    def _init_subparser(self):
        subparser=self._todotracker.subparser
        parser=subparser.add_parser('addtask',help='addtask options')
        parser.add_argument('-P','--project',metavar="PROJ",dest='project',action='store',default=None)
        parser.add_argument('-T','--tags',metavar='TAGS',dest='tags',action='store',default=None)
        parser.add_argument('tasktitle',metavar='DESCR',default='Empty Title')

    def handle_command(self,args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.command==self.COMMAND_NAME:
            project=None
            tagdocuments=[]
            if args.project is not None and args.project != '':
                project=args.project
            if args.tags is not None and args.tags != '':
                taglist=args.tags.split(',')
                for i in taglist:
                    tagdoc=TagDocument(tag=i).save()
                    tagdocuments.append(tagdoc)
            task=TaskDocument()
            task.title=args.tasktitle
            task.project=project
            task.status='New'
            task.created_at=datetime.datetime.utcnow()
            task.updated_at=task.created_at
            task.tags=tagdocuments
            task.save()

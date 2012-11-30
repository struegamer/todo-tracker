import argparse
import datetime
from todotracker.lib import Command

from todotracker.db.models import ProjectDocument

class AddProject(Command):
    COMMAND_NAME = 'add'

    def _init_subparser(self):
        parser = self._parser.add_parser('add', help='Add Options')
        parser.add_argument('projectname', metavar='PROJECTNAME', default='Empty Title')

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            p = ProjectDocument()
            p.title = args.projectname
            p.created_at = datetime.datetime.utcnow()
            p.save()





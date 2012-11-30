import argparse
import datetime
from todotracker.lib import Command

from todotracker.db.models import ProjectDocument

class ListProject(Command):
    COMMAND_NAME = 'list'

    def _init_subparser(self):
        parser = self._parser.add_parser(self.COMMAND_NAME, help='List Options')


    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            project_list = ProjectDocument.objects
            for project in project_list:
                print('{0}'.format(project.title))




import sys
import argparse

try:
    from mongoengine import connect as mongo_connect
except ImportError as e:
    print('You don\'t have mongoengine installed')
    sys.exit(1)

from factories import Commands

class TodoTracker(object):
    def __init__(self):
        self._parser = self._init_parser()
        self._subparser = self._init_subparser(self._parser)
        self._init_mongo()
        self._init_commands()

    @property
    def parser(self):
        return self._parser

    @property
    def subparser(self):
        return self._subparser

    def _init_parser(self):
        parser = argparse.ArgumentParser()
        return parser

    def _init_subparser(self, parser=None):
        if parser is None:
            raise ValueError('parser can\'t be None')
        subparser = parser.add_subparsers(dest='command', title='Commands')
        return subparser

    def _init_commands(self):
        self._cfactory = Commands(self._subparser)
        self._cfactory.add_command(command_class='Task')
        self._cfactory.add_command(command_class='Project')
        self._cfactory.add_command(command_class='Work')

    def _init_mongo(self):
        self._mongo_connection = mongo_connect('todotracker')

    def parse(self):
        args = self._parser.parse_args()
        if args.command in self._cfactory.commandnames:
            try:
                self._cfactory.get_command_handler(args.command).handle_command(args)
            except Exception as e:
                print('Error: {0} ({1})'.format(e, e.__class__.__name__))





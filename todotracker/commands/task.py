import argparse
import datetime
from todotracker.factories import Commands as SubCommands
from todotracker.lib import Command

from todotracker.db.models import TaskDocument
from todotracker.db.models import TagDocument

class Task(Command):
    COMMAND_NAME = 'task'

    def _init_subparser(self):
        self._command_parser = self._parser.add_parser('task', help='Task Options')
        self._subcommand_parser = self._command_parser.add_subparsers(dest='sub_command', help='Task Commands')
        self._init_subcmd_factory()

    def _init_subcmd_factory(self):
        self._subcmd = SubCommands(self._subcommand_parser)
        self._subcmd.add_command('todotracker.subcommands.task', 'AddTask')
        self._subcmd.add_command('todotracker.subcommands.task', 'ListTask')
        self._subcmd.add_command('todotracker.subcommands.task', 'ShowTask')

    def handle_command(self, args=None):
        if args.command == self.COMMAND_NAME:
            if args.sub_command in self._subcmd.commandnames:
                self._subcmd.get_command_handler(args.sub_command).handle_command(args)


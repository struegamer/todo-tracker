import argparse
import datetime
from todotracker.factories import Commands as SubCommands
from todotracker.lib import Command


class Project(Command):
    COMMAND_NAME = 'project'

    def _init_subparser(self):
        self._command_parser = self._parser.add_parser(self.COMMAND_NAME, help='Project options')
        self._subcommand_parser = self._command_parser.add_subparsers(dest='sub_command', help='Project Commands')
        self._init_subcmd_factory()

    def _init_subcmd_factory(self):
        self._subcmd = SubCommands(self._subcommand_parser)
        self._subcmd.add_command('todotracker.subcommands.project', 'AddProject')
        self._subcmd.add_command('todotracker.subcommands.project', 'ListProject')
    def handle_command(self, args=None):
        if args.command == self.COMMAND_NAME:
            if args.sub_command in self._subcmd.commandnames:
                self._subcmd.get_command_handler(args.sub_command).handle_command(args)


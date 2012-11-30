import os
import argparse

from todotracker.lib import Command

from todotracker.db.models import TaskDocument
from todotracker.db.models import TagDocument


class ListTask(Command):
    COMMAND_NAME = 'list'
    STATUS_CHOICES = ['new', 'pending', 'pausing', 'waiting', 'done']

    def _init_subparser(self):
        subparser = self._parser
        parser = subparser.add_parser('list', help='List Options')
        parser.add_argument('listtype', choices=['short', 'long', 'detail'], default='short', nargs='?')
        parser.add_argument('-S', '--status', choices=self.STATUS_CHOICES, dest='status', default='all', action='store', help='List only Tasks with status STATUS')

    @property
    def screen_cols(self):
        def ioctl_GWINSZ(fd):
            try:
                import fcntl, termios, struct, os
                cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            except:
                return None
            return cr
        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)
            except:
                pass
        if not cr:
            try:
                cr = (os.environ['LINES'], os.environ['COLUMNS'])
            except:
                return None
        return int(cr[1])

    def handle_command(self, args=None):
        if args is None:
            raise ValueError('args can\'t be None')
        if args.sub_command == self.COMMAND_NAME:
            self._generate_list(args.listtype, args.status)

    def _short_output(self, format, task):
        print(format.format(task.counter, task.status, task.title))

    def _long_output(self, format, task):
        print(format.format(task.counter, task.status, task.title, task.created_at.strftime('%Y-%m-%d %H:%M:%S'), task.updated_at.strftime('%Y-%m-%d %H:%M:%S')))

    def _detail_output(self, format, task):
        print(format.format(task.counter,
                            task.status,
                            task.title,
                            task.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                            task.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                            ','.join([tag.tag for tag in task.tags])))

    def _output(self, listtype, format, task):
        if listtype == 'long':
            self._long_output(format, task)
        if listtype == 'short':
            self._short_output(format, task)
        if listtype == 'detail':
            self._detail_output(format, task)

    def _generate_list(self, listtype='short', status='all'):
        format = ''
        if listtype == 'short':
            format = '{0:>10} {1:<10} {2:<40}'
            print(format.format('ID', 'Status', 'Task'))
        if listtype == 'long':
            format = '{0:>10} {1:<10} {2:<40} {3:^20} {4:^20}'
            print(format.format('ID', 'Status', 'Task', 'Created at', 'Updated At'))
        if listtype == 'detail':
            format = '{0:>10} {1:<10} {2:<40} {3:^20} {4:^20} {5:<30}'
            print(format.format('ID', 'Status', 'Task', 'Created at', 'Updated At', 'Tags'))
        print('{0:=<{1}}'.format('', self.screen_cols))
        if status != 'all' and status not in self.STATUS_CHOICES:
            raise ValueError('{0} is not a valid status. Valid states are {1}'.format(status, self.STATUS_CHOICES))
        tasklist = []
        if status == 'all':
            tasklist = TaskDocument.objects
        else:
            tasklist = TaskDocument.objects(status=status)
        for task in tasklist:
            self._output(listtype, format, task)
        print('{0:=<{1}}'.format('', self.screen_cols))
        print('Number of Tasks: {0:>10}'.format(len(tasklist)))



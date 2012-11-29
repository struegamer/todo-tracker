import os
import argparse

from command import Command

from todotracker.db.models import TaskDocument
from todotracker.db.models import TagDocument


class ShowTask(Command):
    COMMAND_NAME='show'

    def _init_subparser(self):
        subparser=self._todotracker.subparser
        parser=subparser.add_parser('show',help='Show Options')
        parser.add_argument('task',metavar='TASK_ID')
        parser.add_argument('details',default=None,nargs='?')

    def _output(self,task):
        title='Task: {0}'.format(task.title)
        headline='{0:=<80}'.format('')
        counter='\tID: {0} (UUID: {1})'.format(task.counter,task.id)
        status='\tStatus: {0}'.format(task.status)
        created='\tCreated At: {0}'.format(task.created_at.strftime('%Y-%m-%d %H:%M:%S'))
        updated='\tUpdated At: {0}'.format(task.updated_at.strftime('%Y-%m-%d %H:%M:%S'))
        tags='\tTags: {0}'.format(', '.join([tag.tag for tag in task.tags]))
        print(title)
        print(headline)
        print(counter)
        print(status)
        print(created)
        print(updated)
        print(tags)

    def _output_todos(self,task):
        title='Task: {0}'.format(task.title)
        headline='{0:=<80}'.format('')
        todos='\tTodos:'
        print(title)
        print(headline)
        print(todos)
        for i in task.todos:
            todolist='\t\t{0}'.format(i.title)

    def handle_command(self,args=None):
        if args is None:
            raise ValueError('args can not be None')
        if args.command==self.COMMAND_NAME:
            task=TaskDocument.objects.get(counter=args.task)
            if args.details is None:
                self._output(task)
            if args.details == 'todos':
                self._output_todos(task)
 

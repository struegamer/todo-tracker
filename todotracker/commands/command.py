import argparse

class Command(object):
    COMMAND_NAME='command'

    def __init__(self, todotracker=None):
        self._todotracker=todotracker
        self._init_subparser()

    @property
    def command_name(self):
        return self.COMMAND_NAME

    def _init_subparser(self):
        pass

    def handle_command(self,args=None):
        pass




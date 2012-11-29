
class Commands(object):
    def __init__(self,todotracker=None):
        self._todotracker=todotracker
        self._commands={}

    @property
    def commandnames(self):
        return self._commands.keys()

    def get_command_handler(self, command_name=None):
        if command_name is None:
            raise ValueError('command_name can\'t be None')
        if command_name in self.commandnames:
            return self._commands[command_name]

    def add_command(self,command_class=None):
        try:
            a=__import__('todotracker.commands',globals(),locals(),[command_class],-1)
            cmd=eval('a.{0}'.format(command_class))(self._todotracker)
            print cmd.command_name
            self._commands[cmd.command_name]=cmd
        except Exception,e:
            print e

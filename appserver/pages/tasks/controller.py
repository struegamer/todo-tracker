from todotracker.db.models import TaskDocument

class TaskController(object):
    def __init__(self):
        pass

    def list_all(self, start=0, count=100):
        tasklist = TaskDocument.objects[start:count]
        dictlist = [task.to_dict() for task in tasklist]
        return dictlist

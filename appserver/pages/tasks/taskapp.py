from flask import Blueprint

from views import TaskAPI

Tasks = Blueprint('tasks', __name__)
taskapi = TaskAPI.as_view('task_api')
Tasks.add_url_rule('/tasks/', defaults={'id':None},
                   view_func=taskapi, methods=['GET', ])


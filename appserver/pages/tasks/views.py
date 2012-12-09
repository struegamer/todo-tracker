import json

from flask.views import MethodView
from flask import Response

from controller import TaskController

class TaskAPI(MethodView):
    def get(self, id=None):
        ctrl = TaskController()
        if id is None:
            tasklist = ctrl.list_all()
            js = json.dumps(tasklist)
            resp = Response(js, status=200, mimetype='application/json; charset=utf-8')
            return resp
        else:
            pass



from mongoengine import connect as mongo_connect

from flask import Flask
from pages.tasks import Tasks
from pages.frontend import Frontend

app = Flask(__name__)
app.register_blueprint(Tasks)
app.register_blueprint(Frontend)
app.debug = True
mongo_connect('todotracker')


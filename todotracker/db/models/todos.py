from mongoengine import Document
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import SequenceField
from mongoengine import DateTimeField

class TodoDocument(Document):
    title=StringField()
    status=StringField(choices=['Started','Paused','Finished'])
    started=DateTimeField()
    finished=DateTimeField()


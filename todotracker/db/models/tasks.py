from mongoengine import Document
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import SequenceField
from mongoengine import DateTimeField

from tags import TagDocument
from todos import TodoDocument

class TaskDocument(Document):
    counter=SequenceField()
    title=StringField()
    project=StringField()
    status=StringField(choices=['New','Pending','Waiting','Done'])
    tags=ListField(ReferenceField(TagDocument))
    todos=ListField(ReferenceField(TodoDocument))
    created_at=DateTimeField()
    updated_at=DateTimeField()




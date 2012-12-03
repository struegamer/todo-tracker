from mongoengine import Document
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import SequenceField
from mongoengine import DateTimeField

from tags import TagDocument
from todos import TodoDocument
from projects import ProjectDocument

class TaskDocument(Document):
    counter = SequenceField()
    title = StringField()
    project = ReferenceField(ProjectDocument)
    status = StringField(choices=['new', 'pending', 'pausing', 'waiting', 'done'])
    tags = ListField(ReferenceField(TagDocument))
    created_at = DateTimeField()
    updated_at = DateTimeField()




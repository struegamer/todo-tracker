from mongoengine import Document
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import SequenceField
from mongoengine import DateTimeField

class ProjectDocument(Document):
    title = StringField()
    created_at = DateTimeField()


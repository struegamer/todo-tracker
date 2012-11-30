from mongoengine import Document
from mongoengine import EmbeddedDocument
from mongoengine import EmbeddedDocumentField
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import SequenceField
from mongoengine import DateTimeField

from tasks import TaskDocument

class WorkTimeLog(EmbeddedDocument):
	start = DateTimeField()
	stop = DateTimeField()

class WorkDocument(Document):
    title = StringField()
    status = StringField(choices=['new', 'started', 'stopped'])
    created_at = DateTimeField()
    task = ReferenceField(TaskDocument)
    timelog = ListField(EmbeddedDocumentField(WorkTimeLog))




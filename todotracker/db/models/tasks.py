from mongoengine import Document
from mongoengine import StringField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import SequenceField
from mongoengine import DateTimeField

from tags import TagDocument
from todos import TodoDocument
from projects import ProjectDocument
import datetime


import json
class TaskDocument(Document):
    counter = SequenceField()
    title = StringField()
    project = ReferenceField(ProjectDocument)
    status = StringField(choices=['new', 'pending', 'pausing', 'waiting', 'done'])
    tags = ListField(ReferenceField(TagDocument))
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=datetime.datetime.utcnow())
    user = StringField()

    def to_dict(self):
        rec = {'id':str(self.id).decode('unicode-escape'),
             'counter':str(self.counter).decode('unicode-escape'),
             'title':self.title,
             'project_id':str(self.project.id).decode('unicode-escape') if self.project is not None else '',
             'status':self.status,
             'tags_ref':[str(tag.id).decode('unicode-escape') for tag in self.tags],
             'created_at':self.created_at.isoformat().decode('unicode-escape'),
             'updated_at':self.updated_at.isoformat().decode('unicode-escape'),
             'user':self.user}
        return rec



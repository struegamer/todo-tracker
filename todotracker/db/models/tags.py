from mongoengine import Document
from mongoengine import StringField
from mongoengine import DateTimeField

import datetime

class TagDocument(Document):
    tag = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow())




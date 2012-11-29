from mongoengine import Document
from mongoengine import StringField

class TagDocument(Document):
    tag=StringField()



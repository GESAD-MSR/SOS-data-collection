from mongoengine import Document, StringField, ListField


class Technology(Document):
    name = StringField()
    tags = ListField()

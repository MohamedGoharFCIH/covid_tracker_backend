import mongoengine as db
from .medicine import Medicine
import datetime


class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    temperature = db.IntField()
    lat = db.FloatField()
    lng = db.FloatField()
    age = db.FloatField()
    created_at = db.DateField(default=datetime.datetime.utcnow)
    updated_at = db.DateField(default=datetime.datetime.utcnow)
    medicines = db.ListField(db.ReferenceField(Medicine))

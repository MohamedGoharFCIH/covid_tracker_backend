from app import db 
import datetime


class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    temperature = db.IntField()
    lat = db.FloatField()
    lng = db.FloatField()
    age = db.IntField()
    created_at = db.DateField(default=datetime.datetime.utcnow)
    updated_at = db.DateField(default=datetime.datetime.utcnow)
    medicines = db.ListField(db.ReferenceField('Medicine'))
    def __unicode__(self):
        return self.name
    

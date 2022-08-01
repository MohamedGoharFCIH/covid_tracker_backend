from app import db
import datetime

class Medicine(db.Document):
    name = db.StringField(required=True)
    description = db.StringField()
    created_at = db.DateField(default=datetime.datetime.utcnow)
    updated_at = db.DateField(default=datetime.datetime.utcnow)
    
    def __unicode__(self):
        return self.name
import mongoengine as db

class Medicine(db.Document):
    name = db.StringField(required=True)
    description = db.StringField()

from google.appengine.ext import db
#Table for users
class Person(db.Model):
    firstName = db.StringProperty(required=True)
    lastName = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    dues_paid = db.BooleanProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
class Gear(db.Model):
    number = db.StringProperty(required=True)
    description = db.TextProperty()
    holder = db.ReferenceProperty(Person)
    holderName = db.StringProperty(required=False)
    returnDate = db.DateTimeProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    size = db.FloatProperty(required=False)

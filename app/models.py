from appengine_django.models import BaseModel
from google.appengine.ext import db

class Venue(BaseModel):
  name = db.StringProperty()
  #description = db.TextProperty()
  #address = db.PostalAddressProperty()
  #geopt = db.GeoPtProperty()

class Event(BaseModel):
  name = db.StringProperty()
  tagline = db.StringProperty()
  description = db.TextProperty()
  when = db.DateTimeProperty()
  where = db.ReferenceProperty(Venue)
  #website = db.LinkProperty()
  #contact_email = db.EmailProperty()
  #contact_phone = db.PhoneNumberProperty()

import sys
from appengine_django.models import BaseModel
from google.appengine.ext import db
from google.appengine.ext.db.polymodel import PolyModel
from datetime import timedelta
from urllib import urlopen, quote_plus

# helper methods
def to_geopt(address):
  q = quote_plus(address)
  request = "http://maps.google.se/maps/geo?q=%s&output=csv" % q
  
  try:
    data = urlopen(request).read().split(',')
    if data[0] == '200':
      return GeoPt(data[2], data[3])
    else:
      return None
  except IOError:
    return None
    
class Tag(BaseModel):
  count = db.IntegerProperty(default=0)
  
  def _get_name(self):
    return self.key().name()
  
  @classmethod
  def get_by_name(cls, tagname):
    return cls.get_by_key_name(tagname.lower())
    
  name = property(_get_name)
  
class Taggable(PolyModel):
  tags = db.ListProperty(db.Key)
  
  def add_tag(self, tagname):
    tag = Tag.get_or_insert(tagname.lower())
    if tag.key() not in self.tags:
      self.tags.append(tag.key())
      tag.count += 1 # FIXME: needs to be transactional
      tag.save()
      
  def remove_tag(self, tagname):
    tag = Tag.get_by_name(tagname.lower())
    if tag == None:
      raise ValueError, "%s is not a tag" % tagname
    if tag.key() in self.tags:
      self.tags.remove(tag.key())
      tag.count -= 1
      tag.save() # XXX: Also remove tag if count = 0?
      
  @classmethod  
  def all_for_tag(cls, tagname):
    tag = Tag.get_by_name(tagname.lower())
    return cls.all().filter('tags = ', tag)

class Venue(BaseModel):
  name = db.StringProperty(required=True)
  address = db.PostalAddressProperty(required=True)
  coordinates = db.GeoPtProperty()

class Event(Taggable):
  name = db.StringProperty(required=True)
  description = db.TextProperty(required=True)
  when = db.DateTimeProperty(required=True)
  where = db.ReferenceProperty(reference_class=Venue, required=True)
  website = db.LinkProperty()
  contact_email = db.EmailProperty()
  contact_phone = db.PhoneNumberProperty()
  
  @classmethod
  def all_from(cls, date):
    return Event.all().filter('when >= ', date)
  
  @classmethod
  def all_between(cls, date1, date2):
    return Event.all_from(date1).filter('when < ', date2)
  
  @classmethod
  def all_for(cls, date):
    next_day = date + timedelta(days=1)
    return Event.all_between(date, next_day)
    
  
  

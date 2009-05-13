from google.appengine.ext import db
from datetime import timedelta
from urllib import urlopen, quote_plus

# helper methods
def to_geopt(address):
  q = quote_plus(unicode(address).encode("utf-8"))
  request = 'http://maps.google.se/maps/geo?q=%s&output=csv' % q
  
  try:
    data = urlopen(request).read().split(',')
    if data[0] == '200':
      return db.GeoPt(data[2], data[3])
    else:
      return None
  except IOError:
    return None
    
class Tag(db.Model):
  count = db.IntegerProperty(default=0)
  
  def _get_name(self):
    return self.key().name()
  
  @classmethod
  def get_by_name(cls, tagname):
    return cls.get_by_key_name(tagname.lower())
    
  name = property(_get_name)
  
class Taggable(db.polymodel.PolyModel):
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
      raise ValueError, '%s is not a tag' % tagname
    if tag.key() in self.tags:
      self.tags.remove(tag.key())
      tag.count -= 1
      tag.save() # XXX: Also remove tag if count = 0?
      
  @classmethod  
  def all_for_tag(cls, tagname):
    tag = Tag.get_by_name(tagname.lower())
    return cls.all().filter('tags = ', tag)

class Venue(db.Model):
  name = db.StringProperty(required=True)
  address = db.PostalAddressProperty(required=True)
  coordinates = db.GeoPtProperty()
  
  def __init__(self, *args, **kwds):
    if not kwds.has_key('coordinates'):
      kwds['coordinates'] = to_geopt(kwds['address'])
    db.Model.__init__(self, *args, **kwds)

class Event(Taggable):
  name = db.StringProperty(required=True)
  description = db.TextProperty(required=True)
  date = db.DateProperty(required=True)
  time = db.TimeProperty(required=True)
  venue = db.ReferenceProperty(reference_class=Venue, required=True, collection_name='events')
  website = db.LinkProperty()
  contact_email = db.EmailProperty()
  contact_phone = db.PhoneNumberProperty()
  
  @classmethod
  def all_from(cls, date):
    return Event.all().filter('date >= ', date).order('-date')
  
  @classmethod
  def all_between(cls, date1, date2):
    return Event.all_from(date1).filter('date < ', date2)
  
  @classmethod
  def all_for(cls, date):
    next_day = date + timedelta(days=1)
    return Event.all_between(date, next_day)
    
  
  

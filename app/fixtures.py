# -*- coding: utf-8 -*-

from app.models import Venue, Event
from google.appengine.ext.db import *
from datetime import datetime

chalmers = Venue(
  name=u"Chalmers Tekniska Högskola",
  address=PostalAddress(u"Chalmersplatsen 1, Göteborg"),
)
chalmers.save()

kth = Venue(
  name=u"KTH",
  address=PostalAddress(u"SE-100 44 Stockholm"),
)
kth.save()

svenska_massan = Venue(
  name=u"Svenska Mässan",
  address=PostalAddress(u"Korsvägen Göteborg"),
)
svenska_massan.save()

ncpc = Event(
  name = u"Nordic Collegiate Programming Challenge (NCPC) 2009",
  description = "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. " \
  "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.",
  when = datetime(2009,5,8,18,0),
  where = chalmers,
  website = Link("http://ncpc.example.com"),
  contact_email = Email("foo@example.com"),
  contact_phone = PhoneNumber("46 (31) 111222333"),
)
ncpc.add_tag("java")
ncpc.add_tag("smalltalk")
ncpc.add_tag("python")
ncpc.save()

nordic_python = Event(
  name = u"Nordic Python Conference",
  description = "Lorem ipsum dolor sit amet",
  when = datetime(2009,9,28,10,0),
  where = kth,
  website = None,
  contact_email = None,
  contact_phone = None,
)
nordic_python.add_tag("python")
nordic_python.save()

foobar = Event(
  name = "The Foo Bar",
  description = "Foo bar baz foo bar baz",
  when = datetime(2008,10,18,0,0),
  where = svenska_massan,
  website = None,
  contact_email = None,
  contact_phone = None,
)
foobar.add_tag("ruby")
foobar.save()

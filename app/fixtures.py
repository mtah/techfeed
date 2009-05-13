# -*- coding: utf-8 -*-

from app.models import Venue, Event
from google.appengine.ext.db import *
from datetime import datetime, date, time, timedelta

now = datetime.now()
just_before = now - timedelta(hours=1)
just_after = now - timedelta(hours=1)
later = now + timedelta(days=1)
much_later = now + timedelta(days=5)

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
  name = u"Nordic Collegiate Programming Challenge (NCPC)",
  description = "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. " \
  "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.",
  date = date(now.year,now.month,now.day),
  time = time(now.hour, now.minute),
  venue = chalmers,
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
  date = date(just_before.year,just_before.month,just_before.day),
  time = time(just_before.hour, just_before.minute),
  venue = kth,
  website = None,
  contact_email = None,
  contact_phone = None,
)
nordic_python.add_tag("python")
nordic_python.save()

foobar = Event(
  name = "The Foo Bar",
  description = "Foo bar baz foo bar baz",
  date = date(just_after.year,just_after.month,just_after.day),
  time = time(just_after.hour, just_after.minute),
  venue = svenska_massan,
  website = None,
  contact_email = None,
  contact_phone = None,
)
foobar.add_tag("c++")
foobar.save()

railsconf = Event(
  name = u"RailsConf",
  description = "Lorem ipsum dolor sit amet",
  date = date(later.year,later.month,later.day),
  time = time(later.hour, later.minute),
  venue = kth,
  website = "http://railsconf.org",
  contact_email = "foo@barsson.com",
  contact_phone = None,
)
railsconf.add_tag("ruby")
railsconf.add_tag("rails")
railsconf.save()

barcamp = Event(
  name = u"Barcamp",
  description = "Lorem ipsum dolor sit amet",
  date = date(much_later.year,much_later.month,much_later.day),
  time = time(much_later.hour, much_later.minute),
  venue = chalmers,
  website = "http://barcamp.org",
  contact_email = "foo@barsson.com",
  contact_phone = None,
)
barcamp.add_tag("open source")
barcamp.add_tag("ubuntu")
barcamp.save()


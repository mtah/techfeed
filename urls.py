# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
  (r'^$', 'index'),
  (r'^events/create', 'create_event'),
  (r'^events/(?P<key>.+)', 'show_event'),
  (r'^events', 'list_events'),
  (r'^tags/(?P<tagname>.+)', 'events_for_tag'),
  (r'^venues/(?P<key>.+)', 'show_venue'),
)

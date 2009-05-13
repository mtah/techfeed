from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object
from datetime import datetime, timedelta
from app.models import Event, Venue
from app.forms import EventForm
from app.const import THEM_ALL

def index(request):
  today = datetime.now().date()
  tomorrow = today + timedelta(days=1)
  day_after_tomorrow = tomorrow + timedelta(days=1)
  todays_events = Event.all_for(today).fetch(THEM_ALL)
  tomorrows_events = Event.all_for(tomorrow).fetch(THEM_ALL)
  future_events = Event.all_from(day_after_tomorrow).fetch(THEM_ALL)
  
  return render_to_response('index.html', {
    'todays_events': todays_events,
    'tomorrows_events': tomorrows_events,
    'future_events': future_events,
  })
  
## EVENTS
def create_event(request):
  return create_object(request, form_class=EventForm)
  
def list_events(request):
  one_hour_ago = datetime.now() - timedelta(hours=1)
  return object_list(request, Event.all(), paginate_by=25, template_object_name='event')
  
def show_event(request, key):
  return object_detail(request, Event.all(), key, template_object_name='event')
  
def events_for_tag(request, tagname):
  return object_list(request, Event.all_for_tag(tagname), template_object_name='event')
  
def show_venue(request, key):
  return object_detail(request, Venue.all(), key, template_object_name='venue')
    

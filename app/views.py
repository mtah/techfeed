from django.shortcuts import render_to_response
from django.http import Http404
from datetime import datetime, timedelta
from app.models import Event, Venue
from app.const import THEM_ALL

def index(request):
  today = datetime.now().date()
  tomorrow = today + timedelta(days=1)
  day_after_tomorrow = tomorrow + timedelta(days=1)
  todays_events = Event.all_for(today).order('-when').fetch(THEM_ALL)
  tomorrows_events = Event.all_for(tomorrow).order('-when').fetch(THEM_ALL)
  future_events = Event.all_from(day_after_tomorrow).order('-when').fetch(THEM_ALL)
  
  return render_to_response('index.html', {
    'todays_events': todays_events,
    'tomorrows_events': tomorrows_events,
    'future_events': future_events,
  })

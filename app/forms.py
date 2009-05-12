from django import forms
from app.models import Event, Venue, Tag

class EventForm(forms.ModelForm):
  class Meta:
    model = Event

from django import forms
from app.widgets import AutoCompleteInput
from app.models import Event, Tag
from app.const import THEM_ALL

class EventForm(forms.ModelForm):
  tags = forms.CharField(widget=AutoCompleteInput(
                            [t.name for t in Tag.all().fetch(THEM_ALL)],
                            {'multiple': 'true'}
                        ))
  class Meta:
    model = Event
    exclude = ('class',)

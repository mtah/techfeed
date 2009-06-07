from django import forms
from django.utils import simplejson as json
from django.utils.safestring import mark_safe
from django.utils.html import escape

class AutoCompleteInput(forms.TextInput):
  class Media:
    css = {
      'all': ('/css/jquery.autocomplete.css',)
    }
    js = ('/js/jquery.autocomplete.js',)

  def __init__(self, source, options={}):
    if isinstance(source, list):
      self.source = json.dumps(source)
    elif isinstance(source, str):
      self.source = '%s' % escape(source)
    else:
      raise ValueError, 'Source type is not valid'

    self.options = json.dumps(options) 
    self.attrs = {'autocomplete': 'off'}

  def render(self, name, value, attrs={}):
    attrs.update(self.attrs)
    output = super(AutoCompleteInput, self).render(name, value, attrs)
    return output + mark_safe(u'''
        <script type="text/javascript">
          $('#id_%s').autocomplete(%s, %s)
        </script>''' % (name, self.source, self.options)) 
    

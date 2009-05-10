from django.test import TestCase
from app.models import Tag, Event
from app.const import THEM_ALL

class TagTestCase(TestCase):
  fixtures = ['data.json']
  
  def testTagCount(self):
    tag_count = Event.all_for_tag("python").count()
    tag = Tag.get_by_name("python")
    self.assertEqual(tag_count, tag.count)

from django.test import TestCase
from .models import Direction
# Create your tests here.

class DirectionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Direction.objects.create(step = 'mix it up')

    def test_name_label(self):
        direction = Direction.objects.get(id=1)
        field_label = direction._meta.get_field('step').verbose_name
        self.assertEquals(field_label, 'step')
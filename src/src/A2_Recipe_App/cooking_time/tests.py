from django.test import TestCase
from .models import Cooking_time
# Create your tests here.

class Cooking_timeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cooking_time.objects.create(minutes = '30')

    def test_cooking_time(self):
        cooking_time = Cooking_time.objects.get(id=1)
        expected_object_name = format(cooking_time.minutes)
        self.assertEqual(expected_object_name, '30')
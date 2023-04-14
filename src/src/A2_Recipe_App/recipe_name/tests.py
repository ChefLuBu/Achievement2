from django.test import TestCase
from .models import Recipe_name


# Create your tests here.
class Recipe_nameTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recipe_name.objects.create(name='test')

    def test_name_label(self):
        recipe = Recipe_name.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

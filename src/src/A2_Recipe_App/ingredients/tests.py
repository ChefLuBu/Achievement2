from django.test import TestCase
from .models import Ingredient
# Create your tests here.

class IngredientTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ingredient.objects.create(name='test')

    def test_name_label(self):
        ingredient = Ingredient.objects.get(id=1)
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
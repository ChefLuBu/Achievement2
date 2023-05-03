from django.test import TestCase
from .models import Recipe_app


# Create your tests here.
class Recipe_appTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Recipe_app.objects.create(name='test')
        Recipe_app.objects.create(directions = 'mix it up')
        Recipe_app.objects.create(ingredient_name = 'cheese')
        Recipe_app.objects.create(minutes = '30')


    def test_name_label(self):
        recipe = Recipe_app.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_label(self):
        ingredient_name = Recipe_app.objects.get(id=1)
        field_label = ingredient_name._meta.get_field('ingredient name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_label(self):
        directions = Recipe_app.objects.get(id=1)
        field_label = directions._meta.get_field('directions').verbose_name
        self.assertEquals(field_label, 'step')  
                

    def test_cooking_time(self):
        minutes = Recipe_app.objects.get(id=1)
        expected_object_name = format(Recipe_app.minutes)
        self.assertEqual(expected_object_name, '30')
from django.db import models
from django.core.exceptions import ValidationError


def validate_minutes(value):
    if value % 1 != 0 or value <= 0:
        raise ValidationError('Value must be a positive integer representing minutes.')
    

# Create your models here.
class Recipe_app(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="recipe_name", default='no_picture.jpg')
    ingredient_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    unit_of_measurement = models.CharField(max_length=200)
    directions = models.CharField(max_length=2000)
    minutes = models.PositiveIntegerField(validators=[validate_minutes])


    def __str__(self):
        return self.name
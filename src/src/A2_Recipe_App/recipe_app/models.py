from django.db import models
from django.core.exceptions import ValidationError


def validate_minutes(value):
    if value % 1 != 0 or value <= 0:
        raise ValidationError('Value must be a positive integer representing minutes.')
    

# # Create your models here.
# class Recipe_app(models.Model):
#     name = models.CharField(max_length=200)
#     pic = models.ImageField(upload_to="recipe_name", default='no_picture.jpg')
#     ingredient_name = models.CharField(max_length=200)
#     quantity = models.CharField(max_length=200)
#     unit_of_measurement = models.CharField(max_length=200)
#     directions = models.CharField(max_length=2000)
#     minutes = models.PositiveIntegerField(validators=[validate_minutes])



#     def __str__(self):
#         return self.name
    

    
class Recipe_app(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='recipe_name', default="no_picture.jpg")
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    directions = models.TextField()
    minutes = models.PositiveIntegerField(validators=[validate_minutes])

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit_of_measurement = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe_app, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f'{self.recipe} - {self.ingredient}: {self.quantity} {self.ingredient.unit_of_measurement}'
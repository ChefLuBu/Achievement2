from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


def validate_minutes(value):
    if value % 1 != 0 or value <= 0:
        raise ValidationError("Value must be a positive integer representing minutes.")



class Ingredient(models.Model):
    ingredient_name = models.CharField(default="none listed", max_length=200)


# Create your models here.
class Recipe_app(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="recipe_name", default="no_picture.jpg")
    directions = models.CharField(max_length=2000)
    minutes = models.PositiveIntegerField(validators=[validate_minutes])
    ingredients = models.ManyToManyField(Ingredient, through="Recipe_ingredient")

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(",")
        if self.minutes < 30 and len(ingredients) < 5:
            return "Easy"
        elif self.minutes < 30 and len(ingredients) >= 5:
            return "Medium"
        elif self.minutes >=30 and len(ingredients) < 5:
            return "Intermediate"
        elif self.minutes >=30 and len(ingredients) >= 5:
            return "Hard"
        return difficulty

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_app:recipe_detail', kwargs={'pk': self.pk})


class Recipe_ingredient(models.Model):
    quantity = models.FloatField(default=0)
    unit_of_measurement = models.CharField(default="none listed", max_length=200)
    recipe = models.ForeignKey(
        "Recipe_app", on_delete=models.CASCADE, default="none listed"
    )
    ingredient = models.ForeignKey(
        "Ingredient", on_delete=models.CASCADE, default="none listed"
    )

    
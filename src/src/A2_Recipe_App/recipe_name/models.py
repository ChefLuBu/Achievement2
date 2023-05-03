from django.db import models

# Create your models here.
class Recipe_name(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="recipe_name", default='no_picture.jpg')

    def __str__(self):
        return self.name
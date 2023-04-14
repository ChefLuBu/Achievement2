from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    unit_of_measurement = models.CharField(max_length=200)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class Direction(models.Model):
    step = models.CharField(max_length=2000)

    def __str__(self):
        return self.step
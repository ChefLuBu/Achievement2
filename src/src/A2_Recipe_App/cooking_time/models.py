from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
def validate_minutes(value):
    if value % 1 != 0 or value <= 0:
        raise ValidationError('Value must be a positive integer representing minutes.')
    
class Cooking_time(models.Model):
    minutes = models.PositiveIntegerField(validators=[validate_minutes])

    def __int__(self):
        return self.minutes
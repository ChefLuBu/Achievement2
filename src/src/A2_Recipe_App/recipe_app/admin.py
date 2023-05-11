from django.contrib import admin
from .models import Recipe_app, Recipe_ingredient, Ingredient
# Register your models here.

admin.site.register(Recipe_app)
admin.site.register(Recipe_ingredient)
admin.site.register(Ingredient)
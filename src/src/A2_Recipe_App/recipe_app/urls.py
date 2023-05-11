from django.urls import path 
from .views import home, recipe_detail

app_name = 'recipe_app'

urlpatterns = [
    path('', home),
    path('recipe_detail/<int:recipe_id>', recipe_detail, name='recipe_detail')
]

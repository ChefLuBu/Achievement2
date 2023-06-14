from django.urls import path 
from .views import home, recipe_detail, recipes_home

app_name = 'recipe_app'

urlpatterns = [
    path('', home, name='home'),
    path('recipes_home/', recipes_home, name='recipes_home'),
    path('recipe_detail/<pk>/', recipe_detail, name='recipe_detail')
]

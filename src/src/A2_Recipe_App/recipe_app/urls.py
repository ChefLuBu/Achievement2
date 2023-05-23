from django.urls import path 
from .views import home, recipe_detail, recipe_home

app_name = 'recipe_app'

urlpatterns = [
    path('', home, name='home'),
    path('recipe_home/', recipe_home, name='recipe_home'),
    path('recipe_detail/<int:pk>/', recipe_detail, name='recipe_detail'),]

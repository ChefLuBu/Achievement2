from django.urls import path 
from .views import home

app_name = 'recipe_app'

urlpatterns = [
    path('', home),
]

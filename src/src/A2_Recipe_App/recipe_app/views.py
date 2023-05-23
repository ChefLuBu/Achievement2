from django.shortcuts import render, get_object_or_404
from .models import Recipe_app
# Create your views here.

def home(request):
        return render(request, 'recipe_app/landing_page.html')

def recipe_home(request):
    recipe=Recipe_app.objects.all()
    context={
        'recipe':recipe
    }
    return render(request, 'recipe_app/recipes_home.html',context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe_app, pk=pk)
    context={
        'recipe':recipe
    }
    return render(request, 'recipe_app/recipe_detail.html',context)


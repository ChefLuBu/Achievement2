from django.shortcuts import render, get_object_or_404
from .models import Recipe_app
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


# Create your views here.

# Create your views here.


def home(request):
        return render(request, 'recipe_app/landing_page.html')


@login_required

def recipes_home(request):
    recipe=Recipe_app.objects.all()
    context={
        'recipe':recipe
    }
    return render(request, 'recipe_app/recipes_home.html',context)

@login_required

def recipe_detail(request, pk):
    recipe=get_object_or_404(Recipe_app, pk=pk)
    recipe_ingredient=recipe.recipe_ingredient_set.all()
    context={
        'recipe':recipe,
        'recipe_ingredient':recipe_ingredient
    }

    return render(request, 'recipe_app/recipe_detail.html', context)

@login_required

def records(request):
    return render(request, 'recipe_app/records.html')
from django.shortcuts import render, get_object_or_404
from .models import Recipe_app
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
from.models import Recipe_app
from .utils import get_recipename_from_id, get_chart


import pandas as pd


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

#the request.POST or None is to make sure that the form is valid
def records(request):
    form=RecipeSearchForm(request.POST or None)
    recipe_app_df=None
    chart=None

    #if the form is valid, then we want to print the recipe name and chart type
    if request.method == 'POST':
        name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')

        qs = Recipe_app.objects.filter(name__icontains=name)
        if qs:
            recipe_app_df = pd.DataFrame(qs.values())
            recipe_app_df['recipe_name'] = recipe_app_df['id'].apply(get_recipename_from_id)

            recipe_app_df=recipe_app_df.to_html()
            chart=get_chart(chart_type, data=recipe_app_df, name='recipe_name', value='minutes')


        #The following block is to get introduced to querysets
        #display in terminal - needed for debugging during development only
        print(name, chart_type)
        print('Now Searching')
        print('Case 1: Output of Recie.app.obects.all()')
        qs = Recipe_app.objects.all()
        print(qs)

        print('Case 2: Output of Recie.app.obects.filter(name__icontains=name)')    
        qs = Recipe_app.objects.filter(name__icontains=name)
        print(qs)

        print('Case 3: Output of qs.vlaues()')
        print(qs.values())

        print('Case 4: Output of qs.vlaues_list()')
        print(qs.values_list())

        print('Case 5: Output of Recipe.objects.get(id=1)')
        obj=Recipe_app.objects.get(id=1)
        print(obj)


    #pass the form to the template
    context={
        'form':form,
        'recipe_app_df':recipe_app_df,
        'chart':chart
    }
    #render the template
    return render(request, 'recipe_app/records.html', context)

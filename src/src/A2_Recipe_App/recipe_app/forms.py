from django import forms

# Create your models here.
CHART__CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart'),
)

# Create your forms here.
class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(label='Recipe Name', max_length=100),
    difficulty = forms.CharField(label='Difficulty', max_length=100),
    chart_type = forms.ChoiceField(choices=CHART__CHOICES, widget=forms.RadioSelect)


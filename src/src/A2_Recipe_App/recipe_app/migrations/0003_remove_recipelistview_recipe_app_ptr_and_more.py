# Generated by Django 4.2 on 2023-07-22 00:32

from django.db import migrations, models
import recipe_app.models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe_app", "0002_recipedetailview_recipelistview"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipelistview",
            name="recipe_app_ptr",
        ),
        migrations.AlterField(
            model_name="recipe_app",
            name="minutes",
            field=models.PositiveIntegerField(
                null=True, validators=[recipe_app.models.validate_minutes]
            ),
        ),
        migrations.DeleteModel(
            name="RecipeDetailView",
        ),
        migrations.DeleteModel(
            name="RecipeListView",
        ),
    ]
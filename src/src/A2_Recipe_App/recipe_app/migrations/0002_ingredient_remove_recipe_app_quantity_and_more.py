# Generated by Django 4.2 on 2023-05-09 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recipe_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("unit_of_measurement", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="recipe_app",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="recipe_app",
            name="unit_of_measurement",
        ),
        migrations.AlterField(
            model_name="recipe_app",
            name="directions",
            field=models.TextField(),
        ),
        migrations.RemoveField(
            model_name="recipe_app",
            name="ingredient_name",
        ),
        migrations.AlterField(
            model_name="recipe_app",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.FloatField()),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipe_app.ingredient",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipe_app.recipe_app",
                    ),
                ),
            ],
            options={
                "unique_together": {("recipe", "ingredient")},
            },
        ),
        migrations.AddField(
            model_name="recipe_app",
            name="ingredient_name",
            field=models.ManyToManyField(
                through="recipe_app.RecipeIngredient", to="recipe_app.ingredient"
            ),
        ),
    ]

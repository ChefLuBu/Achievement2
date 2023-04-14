# Generated by Django 4.2 on 2023-04-14 16:15

import cooking_time.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="cooking_time",
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
                (
                    "minutes",
                    models.PositiveIntegerField(
                        validators=[cooking_time.models.validate_minutes]
                    ),
                ),
            ],
        ),
    ]

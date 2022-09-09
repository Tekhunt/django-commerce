# Generated by Django 4.1 on 2022-09-08 19:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rate",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0),
                ]
            ),
        ),
    ]
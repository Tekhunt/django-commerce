# Generated by Django 4.1 on 2022-09-04 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="username",
        ),
    ]

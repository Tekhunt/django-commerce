# Generated by Django 4.1 on 2022-09-06 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_customer_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="state",
            new_name="status",
        ),
    ]

# Generated by Django 4.1 on 2022-09-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_customuser_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]

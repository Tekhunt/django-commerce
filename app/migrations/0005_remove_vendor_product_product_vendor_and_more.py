# Generated by Django 4.1 on 2022-09-07 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_product_vendor_product_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="product",
        ),
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.vendor",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
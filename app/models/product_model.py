from django.db import models

from .user_model import Vendor


class Product(models.Model):
    status = [
    ("active", "active"),
    ("inactive", "inactive")
    ]
    currencies = [
    ('$', "US Dollars ($)"),
    ]
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    currency = models.CharField(max_length=5, choices=currencies, default="$")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10)
    image = models.URLField()
    inventory = models.IntegerField()
    state = models.CharField(max_length=12, choices=status, default="active")
    shipment_delivery_time = models.CharField(max_length=50)

    def __str__(self):
        return self.name or ""
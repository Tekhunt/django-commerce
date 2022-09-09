from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app.models.product_model import Product
from app.models.user_model import Customer


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rate = models.FloatField(
            validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
        )

    def __str__(self):
        return self.product.name

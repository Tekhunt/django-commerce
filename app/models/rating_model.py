from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app.models.product_model import Product
from app.models.user_model import Customer


class Rating(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
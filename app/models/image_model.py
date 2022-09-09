from django.db import models

from app.models.product_model import Product

class ProductImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.URLField()

    def __str__(self):
        return self.product.name
from django.db import models

from app.models.product_model import Product
from app.models.user_model import Customer


class Like(models.Model):
    """like  comment"""

    post = models.ForeignKey(Product, related_name="likes", on_delete=models.CASCADE)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.name

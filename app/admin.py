from django.contrib import admin
from app.models.product_model import Product

from app.models.user_model import CustomUser, Customer, Vendor


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Product)
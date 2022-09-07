from django.db import models
from wand.image import Image
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.crypto import get_random_string
import sys
from .user_model import Vendor



# def upload_path(instance,title):
#     vendor = instance.vendor
#     product = instance.name
#     if Vendor.id == vendor:
#         new = Vendor.brand
#     return f'public/{new}/{prod}.jpg'


class Product(models.Model):
    status = [("active", "active"), ("inactive", "inactive")]
    currencies = [
        ("$", "US Dollar ($)"),
    ]
    DELEVERY_TIME = [
        ("1-3 Business Days", "1-3 days"),
        ("1-5 Business Days", "1-5 days"),
        ("1-15 Business Days", "1-15 days"),
    ]
    name = models.CharField(max_length=40)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=30, blank=True, null=True)
    currency = models.CharField(max_length=5, choices=currencies, default="$")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10)
    image = models.ImageField(upload_to='static/images')
    inventory = models.IntegerField()
    status = models.CharField(max_length=12, choices=status, default="active")
    shipment_delivery_time = models.CharField(
        max_length=20, choices=DELEVERY_TIME, default="1-5 Business Days"
    )

    def save(self):
        img = Image.open(self.image)

        output = BytesIO()

        img = img.resize((200, 200))

        img.save(output, format="JPEG", quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % self.image.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )
        short_genome = f"{self.name[:3]}{self.category[:3]}"
        self.sku = self.sku+short_genome

        super(Product, self).save()

    def __str__(self):
        return self.name or ""

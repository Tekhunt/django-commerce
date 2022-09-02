from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .user_manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    credit_card = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.email

class Vendor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.email
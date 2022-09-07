from dataclasses import field
from rest_framework import serializers
import pandas as pd
from app.models.cart_model import Cart
from app.models.user_model import CustomUser, Customer, Vendor
from app.models.product_model import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super.update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


# class BulkInstanceSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):

#         df = pd.read_csv('/', sep='delimiter')
#         products = []
#         for i in range(len(df)):
#             products.append(
#                 Product(
#                 name=df.iloc[i][0],
#                 description=df.iloc[i][1],
#                 price=df.iloc[i][2]
#                 )
#             )
#         instance = Product.objects.bulk_create(products)
#         instance.save
#         return instance

#     class Meta:
#         model = Product
#         fields = '__all__'

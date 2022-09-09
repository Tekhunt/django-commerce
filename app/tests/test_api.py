from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.urls import resolve

from app.views import (
    CartDetail,
    CartList,
    ProductImageDetail,
    ProductImageList,
    ProductsDetail,
    ProductsList,
    RegisterApi,
    ReviewDetail,
    ReviewList,
    User,
    UserView,
    UsersData,
    VendorDetail,
    VendorList,
)


class TestSamples(TestCase):
    def test_users_url_is_resolved(self):
        url = reverse("userview")
        self.assertEquals(resolve(url).func.view_class, UserView)

    def test_post_detail_url_is_resolved(self):
        url = reverse("user", args=[1])
        self.assertEquals(resolve(url).func.view_class, User)

    def test_register_url_is_resolved(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func.view_class, RegisterApi)

    def test_userdata_detail_url_is_resolved(self):
        url = reverse("users_data")
        self.assertEquals(resolve(url).func.view_class, UsersData)

    def test_vendor_detail_url_is_resolved(self):
        url = reverse("vendors_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, VendorDetail)

    def test_vendor_url_is_resolved(self):
        url = reverse("vendors_list")
        self.assertEquals(resolve(url).func.view_class, VendorList)

    def test_products_detail_url_is_resolved(self):
        url = reverse("products_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, ProductsDetail)

    def test_products_url_is_resolved(self):
        url = reverse("products_list")
        self.assertEquals(resolve(url).func.view_class, ProductsList)

    def test_cart_url_is_resolved(self):
        url = reverse("cart_list")
        self.assertEquals(resolve(url).func.view_class, CartList)

    def test_cart_detail_url_is_resolved(self):
        url = reverse("cart_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, CartDetail)

    def test_review_url_is_resolved(self):
        url = reverse("review_list")
        self.assertEquals(resolve(url).func.view_class, ReviewList)

    def test_review_detail_url_is_resolved(self):
        url = reverse("review_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, ReviewDetail)

    def test_product_image_url_is_resolved(self):
        url = reverse("product_image_list")
        self.assertEquals(resolve(url).func.view_class, ProductImageList)

    def test_product_image_detail_url_is_resolved(self):
        url = reverse("product_image_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, ProductImageDetail)

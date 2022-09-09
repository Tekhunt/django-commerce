from django.urls import path
from . import views
from .views import (
    CartDetail,
    CartList,
    LoginView,
    LogoutView,
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
    HomeView,
    VendorDetail,
    VendorList,
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("api/register/", RegisterApi.as_view(), name="register"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/userview/", UserView.as_view(), name="userview"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/users/", UsersData.as_view(), name="users_data"),
    path("api/user/<int:pk>/", User.as_view(), name="user"),
    path("api/vendors/", VendorList.as_view(), name="vendors_list"),
    path("api/vendors/<int:pk>/", VendorDetail.as_view(), name="vendors_detail"),
    path("api/products/", ProductsList.as_view(), name="products_list"),
    path("api/products/<int:pk>/", ProductsDetail.as_view(), name="products_detail"),
    path("api/cart/", CartList.as_view(), name="cart_list"),
    path("api/cart/<int:pk>/", CartDetail.as_view(), name="cart_detail"),
    path("api/review/", ReviewList.as_view(), name="review_list"),
    path("api/review/<int:pk>/", ReviewDetail.as_view(), name="review_detail"),
    path("api/product-image/", ProductImageList.as_view(), name="product_image_list"),
    path("api/product-image/<int:pk>/", ProductImageDetail.as_view(), name="product_image_detail"),
]

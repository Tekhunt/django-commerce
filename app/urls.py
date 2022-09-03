from django.urls import path
from . import views
from .views import LoginView, LogoutView, ProductsDetail, ProductsList, RegisterApi, User, UserView, UsersData, HomeView, VendorDetail, VendorList


urlpatterns = [
    path('', views.HomeView.as_view(), name ='home'),
    path('api/register/', RegisterApi.as_view()),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/userview/", UserView.as_view(), name="userview"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/users/", UsersData.as_view(), name="users_data"),
    path("api/user/<int:pk>/", User.as_view(), name="user"),
    path("api/vendors/", VendorList.as_view(), name="vendors_list"),
    path("api/vendors/<int:pk>/", VendorDetail.as_view(), name="vendors_detail"),
    path("api/products/", ProductsList.as_view(), name="products_list"),
    path("api/products/<int:pk>/", ProductsDetail.as_view(), name="products_detail"),
]

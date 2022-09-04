from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.contrib.auth import authenticate
from wand.image import Image
from app.models.cart_model import Cart
from app.models.user_model import CustomUser, Vendor
from app.models.product_model import Product
from .serializers import (
    CartSerializer,
    ProductSerializer,
    UserSerializer,
    UserDataSerializer,
    VendorSerializer
)
# from dotenv import load_dotenv

# load_dotenv()


class HomeView(APIView):
    def get(self, request):
        content = {'message': 'Welcome to where awesomeness is cooked!'}
        return Response(content)

class RegisterApi(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(UserSerializer(user, context=self.get_serializer_context()).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class LoginView(APIView):
#     permission_classes = ()

#     def post(self, request,):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(username=email, password=password)
#         if user:
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = CustomUser.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class UsersData(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )

    queryset = CustomUser.objects.all()
    serializer_class = UserDataSerializer

class User(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDataSerializer

class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetail(generics.RetrieveDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ProductsList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer





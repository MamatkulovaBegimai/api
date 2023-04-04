from django.shortcuts import render
from rest_framework import generics
from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterSerializer, UserUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# Create your views here.

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    
class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    # serializer_class = UserUpdateSerializer
    
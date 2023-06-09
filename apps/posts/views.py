from django.shortcuts import render
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from rest_framework import generics

# Create your views here.
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer    
    
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer    
    
class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()    
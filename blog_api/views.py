from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


# first view
class PostList(generics.ListCreateAPIView):
    # performs list and create items

    # tell the view what data we want to use
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass

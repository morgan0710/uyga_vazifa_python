from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializera import AuthorSerializer
# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
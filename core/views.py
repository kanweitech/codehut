from django.shortcuts import render
from django.contrib.auth.models import User
from core.models import Snippet
from core.serializers import SnippetSerializer, UserSerializer
from core.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions


# Using generic class-based views here.
# This is a powerful pattern that allows us to reuse common functionality, and helps us keep our code DRY.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SnippetDetail(generics.RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
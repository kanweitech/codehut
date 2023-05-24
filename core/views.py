from django.shortcuts import render
from core.models import Snippet
from core.serializers import SnippetSerializer
from rest_framework import generics

# Using generic class-based views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
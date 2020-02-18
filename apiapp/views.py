from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class HomeView(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

   
    











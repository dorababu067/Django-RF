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
class HomeView(mixins.ListModelMixin,
            mixins.CreateModelMixin,
            generics.GenericAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DetailView(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    











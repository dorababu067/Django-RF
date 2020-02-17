from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from django.http import HttpResponse, JsonResponse
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class HomeView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        school  = self.get_object(pk)
        serializer = SchoolSerializer(school)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        school = self.get_object(pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        school = self.get_object(pk)
        school.delete()
        return  HttpResponse('Object deleted')









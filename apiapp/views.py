from django.shortcuts import render
from  . models import School
from . serializers import SchoolSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return JsonResponse(serializer.data, safe=False) 
    
    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, id=None):
    try:
        school = School.objects.get(id=id)
    except School.DoesNotExist:
        return HttpResponse("Data not found")
        
    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return JsonResponse(serializer.data, status=200)

    if request.method == 'PUT':
        serializer = SchoolSerializer(school, request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        school.delete()
        return HttpResponse('object deleted')
            
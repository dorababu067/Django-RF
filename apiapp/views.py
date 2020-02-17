from django.shortcuts import render
from  . models import School
from . serializers import SchoolSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'GET':
        schools = School.objects.all()
        # converting model query objects into pytohon object
        serializer = SchoolSerializer(schools, many=True)
        # converting pytohon object into Json data
        return JsonResponse(serializer.data, safe=False) 
    
    elif request.method == 'POST':
        #converting the raw data into python
        data = JSONParser().parse(request) 
        serializer = SchoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def detail(request, id=None):
    try:
        school = School.objects.get(id=id)
    except School.DoesNotExist:
        return HttpResponse("Data not found")
        
    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return JsonResponse(serializer.data, status=200)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SchoolSerializer(school, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        school.delete()
        return HttpResponse('object deleted')
            
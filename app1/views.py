from django.shortcuts import render
from .models import Student
from rest_framework.serializers import Serializer
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def Student_Single(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)


def Student_All(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        Json_data = request.body
        stream = io.BytesIO(Json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(Json_data, content_type='application/json')

        Json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(Json_data, content_type='application/json')

#it will work tests.py file check into app1
@csrf_exempt
def student_detail(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return JsonResponse(serializer.data, safe=False)


    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created !'}
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse(serializer.errors)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data = pythondata, partial=True) #For_partial_update(Not_Required All fields)
        # serializer = StudentSerializer(stu, data = pythondata, partial=True) #For_complete_update(Required All fields)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data updated !!'}
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        if id is not None:
            stu.delete()
            res = {'msg' : 'Data deleted'}
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse(Serializer.errors)

from django.shortcuts import render
from .models import Student
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
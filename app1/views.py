from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_detail(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)


    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created !'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = pythondata, partial=True) #For_partial_update(Not_Required All fields)
        # serializer = StudentSerializer(stu, data = pythondata, partial=True) #For_complete_update(Required All fields)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data updated !!'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_502_BAD_GATEWAY)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        if id is not None:
            stu.delete()
            return Response({'msg' : 'Data deleted'}, status=status.HTTP_302_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

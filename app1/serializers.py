from rest_framework import serializers
from .models import Student
# from rest_framework import routers, serializers, viewsets

# class StudentSerializer(serializers.serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

# from .models import register

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'roll', 'city')

        name = serializers.CharField(max_length=100)
        roll = serializers.IntegerField()
        city = serializers.CharField(max_length=100)
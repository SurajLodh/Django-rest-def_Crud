from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

# def create(self, validated_data):
#     return Student.objects.create(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'roll', 'city')

        # id = serializers.IntegerField()
        name = serializers.CharField(max_length=100)
        roll = serializers.IntegerField()
        city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


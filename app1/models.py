from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

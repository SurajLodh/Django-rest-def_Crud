from django.contrib import admin
from .models import Student

# Register your models here.
# admin.site.register(Student) //old method no use 

#This method to view List_display contains directly in admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
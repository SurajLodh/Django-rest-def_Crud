from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('stuinfo/', views.Student_All),
    path('stuinfo/<int:pk>', views.Student_Single),
    path('create/', views.student_create),
    path('stud/', views.student_detail),
]
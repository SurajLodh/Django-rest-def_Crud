from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_detail),
    path('student/<int:pk>/', views.student_detail),
]
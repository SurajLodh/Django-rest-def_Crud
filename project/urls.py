from django.contrib import admin
from django.urls import path, include
from app1 import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(app1.views)),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.Student_All),
    path('stuinfo/<int:pk>', views.Student_Single),
    path('create/', views.student_create),
]
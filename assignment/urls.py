from django.contrib import admin
from django.urls import path
from assignment import views

urlpatterns = [
    path('api/students', views.StudentListAPIView.as_view() ,name="student"),
    path('api/student-add', views.StudentAdd ,name="student_add"),
]

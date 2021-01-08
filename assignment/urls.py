from django.contrib import admin
from django.urls import path
from assignment import views

urlpatterns = [
    path('api/students', views.StudentListAPIView.as_view() ,name="student"),
    path('api/students/<str:pk>', views.StudentDetail.as_view() ,name="student_detail"),
]

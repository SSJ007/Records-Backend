from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


class StudentListAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        if ('name' in self.request.GET):
            res = self.request.query_params['name']
            return Student.objects.filter(name__istartswith=res)
        elif ('roll' in self.request.GET):
            res = self.request.query_params['roll']
            return Student.objects.filter(roll_no__istartswith=res)
        elif ('sort' in self.request.GET):
            sort = self.request.query_params['sort']
            if sort == 'name_asc':
                return Student.objects.all().order_by('name')
            if sort == 'name_desc':
                return Student.objects.all().order_by('-name')
            if sort == 'maths_asc':
                return Student.objects.all().order_by('maths')
            if sort == 'maths_desc':
                return Student.objects.all().order_by('-maths')
            if sort == 'physics_asc':
                return Student.objects.all().order_by('physics')
            if sort == 'physics_desc':
                return Student.objects.all().order_by('-physics')
            if sort == 'chemistry_asc':
                return Student.objects.all().order_by('chemistry')
            if sort == 'chemistry_desc':
                return Student.objects.all().order_by('-chemistry')
            if sort == 'total_asc':
                return Student.objects.all().\
                annotate(total=F('maths') + F('physics') + F('chemistry')
                ).order_by('total')
            if sort == 'total_desc':
                return Student.objects.all().\
                annotate(total=F('maths') + F('physics') + F('chemistry')
                ).order_by('-total')
        else:
            return Student.objects.all().\
            annotate(total=F('maths') + F('physics') + F('chemistry')
            ).order_by('-total')

    queryset = Student.objects.all().\
            annotate(total=F('maths') + F('physics') + F('chemistry')
            ).order_by('-total')
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


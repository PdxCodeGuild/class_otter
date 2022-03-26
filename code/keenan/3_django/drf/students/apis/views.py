from django.shortcuts import render

from rest_framework import generics,  viewsets
from .serializers import StudentSerializer

from students_app import models


# this is the apis app views.py
# Create your views here.

# class ListStudent(generics.ListCreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer


# class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer

# this replaces both of the above?
class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
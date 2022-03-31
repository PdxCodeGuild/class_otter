from django.shortcuts import render
from rest_framework import viewsets

from students.models import Student

from .serializers import StudentSerializer
from rest_framework import generics


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
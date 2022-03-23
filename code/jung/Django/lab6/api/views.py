from rest_framework import generics

from student import models
from .serializers import StudentSerializer

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ListStudent(generics.ListCreateAPIView):
    filterset_field = ['last_name', 'first_name']
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


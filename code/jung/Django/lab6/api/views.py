from rest_framework import generics

from student import models
from .serializers import StudentSerializer

from django_filters.rest_framework import DjangoFilterBackend


class ListStudent(generics.ListCreateAPIView):
    filterset_fields = ['last_name', 'first_name']
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


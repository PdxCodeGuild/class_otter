from rest_framework import viewsets

from students import models
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
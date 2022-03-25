from rest_framework import generics

from students.models import Student

from .serializers import StudentSerializer

# class StudentAPIView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

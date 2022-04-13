from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Students
from .serializer import StudentSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api'
    ]
    return Response(routes)


@api_view(['GET'])
def getStudents(request):
    student = Students.objects.all()
    serilizer = StudentSerializer(student, many=True)
    return Response(serilizer.data)
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
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

@api_view(['PUT', ])
def api_edit(request, slug):

    try:
        student = Students.objects.get(slug=slug)
    except Students.DoesNotExist:
        return Response(status=HttpResponseNotFound)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        data= {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "edit successful"
            return Response(data=data)

        return Response(serializer.data)

@api_view(['DELETE', ])
def api_delete(request, slug):

    try:
        student = Students.objects.get(slug=slug)
    except Students.DoesNotExist:
        return Response(status=HttpResponseNotFound)
    if request.method == 'DELETE':
        operation = student.delete()
        data= {}
        if operation:
            data["sucess"] = "deletion successful"
        else:
            data["failure"] = "deletion failure"
        return Response(data=data)

@api_view(['POST', ])
def api_new(request, slug):
    student = Students.objects.create()
    if request.method == 'POST':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
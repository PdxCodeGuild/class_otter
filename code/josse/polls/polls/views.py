from django import http
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world!')
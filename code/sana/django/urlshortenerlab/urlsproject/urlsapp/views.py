from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('page')
    return render(request, 'index.html')

def home(request):
    return HttpResponse('home')
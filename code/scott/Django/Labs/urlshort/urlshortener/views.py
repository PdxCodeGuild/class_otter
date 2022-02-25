'''
Shortener views
'''
from django.shortcuts import render, get_object_or_404 # We will use it later
from django.http import HttpResponse 

from .models import Urlshort

def home_view(request):
    return HttpResponse("Testee")
# Create your views here.

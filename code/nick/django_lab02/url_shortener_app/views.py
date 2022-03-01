from types import CodeType
from django import urls
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Url
from django.urls import reverse

def index(request):
    context = {'message': "blah blah blah"}
    return render(request, 'url_shortener_app/index.html', context)


def new(request):
    url = request.POST['description']    
    Url.objects.create(url=url)
    return HttpResponseRedirect(reverse('url_shortener_app:index'))
# Create your views here.
# input/output for url
# convert long code to short code
# url needs to be recorded in database
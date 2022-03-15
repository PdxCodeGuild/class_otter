from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import uuid
from .models import Link


archives = {}

def index(request):
    # return HttpResponse('page')
    return render(request, 'index.html')

def home(request):
    return HttpResponse('home')

def database(inputurl, shorturl):
    archives.update({ f"{shorturl}":f"{inputurl}"})

def process(request): 
    if request.method == 'POST':
        input_url = request.POST['link']
        unique_url = str(uuid.uuid4())[:7]
        new_url = Link(ulink=input_url, slink=unique_url)
        database(input_url, unique_url)
        new_url.save()
        return HttpResponse(unique_url, input_url)

  
def send(request):
    if request.method == 'POST':
        request_url = request.POST['input']
        if request_url in archives:
            accepted_url = archives[request_url]
            return HttpResponseRedirect(accepted_url)
        else:
            return redirect('/')
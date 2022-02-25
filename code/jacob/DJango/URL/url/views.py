from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Shortener

from random import choice
from string import ascii_letters, digits

def index(request):    

    if request.method == 'POST':
        acquired_url = Shortener.objects.all()
        letters = ascii_letters + digits        
        short_url = ''.join(choice(letters) for i in range(6))
        Shortener.objects.create(url_to_shorten=acquired_url, url_short=short_url)
        context = {'acquired_url': acquired_url, 'short_url': short_url}
        return render(request, 'url/index.html', context)
    
    else:
         return render(request, 'url/index.html')





from multiprocessing import context
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Shortener

from random import choice
from string import ascii_letters, digits

def index(request):    

    if request.method == 'POST':
        acquired_url = request.POST['url']
        letters = ascii_letters + digits        
        short_url = ''.join(choice(letters) for i in range(6))
        Shortener.objects.create(url_to_shorten=acquired_url, url_short=short_url)
        all_values = Shortener.objects.all()
        context = {'acquired_url': acquired_url, 'short_url': short_url, 'all_values': all_values}
        return render(request, 'url/index.html', context)
    
    else:
        all_values = Shortener.objects.all()
        context = {'all_values': all_values}
        return render(request, 'url/index.html', context)

def redirect(request, short):
    redirect_url = get_object_or_404(Shortener, url_short=short)
    return HttpResponseRedirect(redirect_url.url_to_shorten)





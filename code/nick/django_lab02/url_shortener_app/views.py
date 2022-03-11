import random
import string
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UrlInfo

# Create your views here.
    # renders template

def short_url(request): 
    if request.method =='POST':
        long_url = request.POST['long_url']
        short_url = ''.join(random.choice(string.ascii_letters)for x in range(5))
        new_url = UrlInfo(long_url=long_url, short_url=short_url)
        new_url.save()
    context = {'long_url':UrlInfo.objects.all()}
    #    0 return render(request, 'url_shortener_app/index.html',context)
    return render(request, 'url_shortener_app/index.html',context)
    # places it in database and generates short code
def forward(request):
    return HttpResponseRedirect()
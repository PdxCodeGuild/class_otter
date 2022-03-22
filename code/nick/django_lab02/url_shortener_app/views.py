import random
import string
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
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
def redirect(request):
    for obj in UrlInfo.objects.all():
        url = obj.long_url
    return HttpResponseRedirect(url)
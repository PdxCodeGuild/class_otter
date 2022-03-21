from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortener
from django.urls import reverse

import uuid

def index(request):
    if request.method == "POST":
        u = uuid.uuid4()
        short_url = str(u)[:6]
        long_url = request.POST["url"]
        new_url = Shortener(long_url = long_url, short_url = short_url)
        new_url.save()
    
        context = {"long_url": long_url, "short_url": short_url}
    else:
        context = {}
    return render(request, "urlshortener/index.html", context)

def redirect(request, short_url):
    url = get_object_or_404(Shortener, short_url = short_url)
    if "https://" in url.long_url:
        url.long_url = url.long_url
    else:
        url.long_url = "https://" + url.long_url

    return HttpResponseRedirect(url.long_url)
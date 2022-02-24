from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Link


def index(request):
    return render(request, 'url_shortener/index.html')

def create(request):
    def generate_code():
        return 'fake_code'

    link = Link.objects.create(url=request.POST['url'], short_code=generate_code())
    return HttpResponseRedirect(reverse('url_shortener:index'))

def link_through(request, short_code):
    link_list = Link.objects.filter(short_code__exact=short_code)
    if len(link_list) <= 0:
        return HttpResponseRedirect(reverse('url_shortener:index'))
    else:
        return redirect(link_list[0].url)

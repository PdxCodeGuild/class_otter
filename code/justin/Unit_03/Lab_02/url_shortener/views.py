from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Link
import random
import string


def index(request):
    return render(request, 'url_shortener/index.html')

class ShortCodeGenerator:
    available_letters = string.ascii_letters.replace('I', '').replace('l', '').replace('O', '')
    available_digits = string.digits.replace('1', '').replace('0', '')
    base57characters = list(available_letters + available_digits)

    @classmethod
    def get(cls):
        code = []
        for i in range(8):
            code.append(random.choice(cls.base57characters))
        random.shuffle(code)
        return ''.join(code)

def create(request):
    link = Link.objects.create(url=request.POST['url'], short_code=ShortCodeGenerator.get())
    return HttpResponseRedirect(reverse('url_shortener:detail', args=(link.short_code,)))

def detail(request, short_code):
    link_list = Link.objects.filter(short_code__exact=short_code)
    if len(link_list) <= 0:
        return HttpResponseRedirect(reverse('url_shortener:index'))
    else:
        context = {'link': link_list[0]}
        return render(request, 'url_shortener/detail.html', context)

def link_through(request, short_code):
    link_list = Link.objects.filter(short_code__exact=short_code)
    if len(link_list) <= 0:
        return HttpResponseRedirect(reverse('url_shortener:index'))
    else:
        return redirect(link_list[0].url)

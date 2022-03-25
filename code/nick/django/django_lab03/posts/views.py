from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Chirp
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context ={'chirps':Chirp.objects.all}
    return render(request,'posts/home.html',context)
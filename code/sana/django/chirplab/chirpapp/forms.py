from django import forms
from .models import chirp
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ChirpListView(LoginRequiredMixin, ListView):
    model = chirp
    template_name = 'chirpapp/home.html'
    ordering = ['-datetime']

class ChirpPostView(LoginRequiredMixin, CreateView):
    model = chirp
    template_name = 'chirpapp/chirp.html'
    fields = ['text']
    sucess_url = '/'


class ChirpForm():
    post = forms.CharField(max_length=200, default='')
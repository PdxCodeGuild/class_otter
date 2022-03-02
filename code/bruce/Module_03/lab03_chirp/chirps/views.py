from attr import field
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chirp

class ChirpListView(ListView):
    model = Chirp
    template_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp_detail.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'chirp_hatch.html'
    fields = ['tiny_body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



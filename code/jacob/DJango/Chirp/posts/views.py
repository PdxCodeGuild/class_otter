from audioop import reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new.html'
    fields = ['whistle']
    success_url = reverse_lazy('chirp:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
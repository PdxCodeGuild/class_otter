from dataclasses import field
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Posts

class BlogListView(ListView):
    model = Posts
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Posts
    template_name = 'detail.html'

class ChirpCreateView(CreateView):
    model = Posts
    template_name = 'new.html'
    fields = ['author','body']

class ChirpEditView(UpdateView):
    model = Posts
    template_name = 'edit.html'
    fields = ['title', 'body']

class ChirpDeleteView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('posts:home')
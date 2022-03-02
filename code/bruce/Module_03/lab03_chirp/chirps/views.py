from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chirp


class ChirpListView(ListView):
    """
    Inherits 'ListView'. We can use 'chirp_list' or 'object_list' to get the queryset in a list template.
    """
    model = Chirp
    template_name = 'home.html'


class ChirpDetailView(DetailView):
    """
    Inherits 'DetailView'. We can use 'chirp' to get the specific 'Chirp' in a detail template.
    """
    model = Chirp
    template_name = 'chirp_detail.html'


class ChirpCreateView(LoginRequiredMixin, CreateView):
    """
    Inherits 'LoginRequiredMixin' and 'CreateView'. 
    """
    model = Chirp
    template_name = 'chirp_hatch.html'
    fields = ['tiny_body', 'author']
    # # Could use:
    # fields = '__all__'

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChirpModerateView(UpdateView):
    model = Chirp
    template_name = 'chirp_moderate.html'
    # Might add other fields here later.
    fields = ['tiny_body']

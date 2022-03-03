from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Chirp

class ChirpListView(ListView):
    model = Chirp
    template_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp_detail.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'chirp_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'chirp_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        chirp = self.get_object()
        return self.request.user == chirp.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'chirp_delete.html'
    success_url = reverse_lazy('chirps:home')

    def test_func(self):
        chirp = self.get_object()
        return self.request.user == chirp.author
# Create your views here.

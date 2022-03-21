from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

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
    Inherits 'LoginRequiredMixin' and 'CreateView'. 'LoginRequiredMixin' verifies user is authenticated, then user is allowed to Create a new Chirp.
    """
    model = Chirp
    template_name = 'chirp_hatch.html'
    # fields = ['tiny_body', 'author']
    fields = ['tiny_body']
    # # Could use:
    # fields = '__all__'

    # We are writing our own modification of form_valid.
    # Setting user who is making the request as the author of the form instance.
    def form_valid(self, form):
        # Django 'knows' that forms can have the same attributes as the model.
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChirpModerateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Inherits 'UpdateView'. Moderate or 'update' a Chirp.
    """
    model = Chirp
    template_name = 'chirp_moderate.html'
    # Might add other fields here later.
    fields = ['tiny_body']

    def test_func(self):
        # Get the Chirp:
        # print(f"type(self): {type(self)}")
        # print(f"self: {self}")
        # print(f"self.get_object(): {self.get_object()}")
        # print(f"self.request.GET: {self.request.GET}")
        # print(f"self.request.GET.keys(): {self.request.GET.keys()}")
        # print(f"self.request: {self.request}")
        # print(f"self.request.method: {self.request.method}")
        # print(f"self.request.META: {self.request.META}")
        chirp = self.get_object()
        # print(f"chirp: {chirp}")
        # Return True if chirp.author is request user:
        print(f"self.request.user: {self.request.user}")
        print(f"chirp.author: {chirp.author}")
        print(f"Requesting user is Chirp author: {self.request.user == chirp.author}")
        return self.request.user == chirp.author



class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Inherits 'DeleteView'. Delete a Chirp.
    """
    model = Chirp
    template_name = 'chirp_delete.html'
    # Function view: reverse()
    # Class view: reverse_lazy()
    success_url = reverse_lazy('chirps:home')

    def test_func(self):
        # Get the Chirp:
        chirp = self.get_object()
        # Return True if chirp.author is request user:
        print(f"self.request.user: {self.request.user}")
        print(f"chirp.author: {chirp.author}")
        print(f"Requesting user is Chirp author: {self.request.user == chirp.author}")
        return self.request.user == chirp.author


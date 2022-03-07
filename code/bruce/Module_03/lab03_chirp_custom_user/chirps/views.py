from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Chirp
from users.models import CustomUser


class ChirpListView(ListView):
    """
    Inherits ''. We can use 'chirp_list' and 'object_list' to get the queryset in the list template.
    """
    model = Chirp
    template_name = 'home.html'


class ChirpDetailView(DetailView):
    """
    Inherits 'DetailView'. We can use 'chirp' to get the specific 'Chirp' in a detail template.
    """
    model = Chirp
    template_name = 'chirp_detail.html'


# 'LoginRequiredMixin' just requires a user to be logged in. It doesn't require them to be any specific user.
# Also, the 'LoginRequiredMixin' may 'do something' each time called before the other class 'CreateView' is called. That's why it's the first (to the left) in the inheritance parentheses.
class ChirpCreateView(LoginRequiredMixin, CreateView):
    """
    Inherits 'LoginRequiredMixin' and 'CreateView'. 'LoginRequiredMixin' verifies user is authenticated, then user is allowed to Create a new Chirp.
    """
    model = Chirp
    template_name = 'chirp_hatch.html'
    fields = ['tiny_body']
    # # Could use:
    # fields = '__all__'

    # We are writing our own modification of 'form_valid'.
    # Documentation says the function is run after valid data is POSTed. I think that means after valid data is received.
    # Setting the value of 'author' of the form instance to be the value of the user who is making the request.
    def form_valid(self, form):
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
        # print(f"type(self): {type(self)}")                            # <class 'chirps.views.ChirpModerateView'>
        # print(f"self: {self}")                                        # <chirps.views.ChirpModerateView object at 0x000001370974A560>
        # print(f"type(self.get_object()): {type(self.get_object())}")  # <class 'chirps.models.Chirp'>
        # print(f"self.get_object(): {self.get_object()}")              # The instance of Chirp class - a 'chirp' object.
        # print(f"self.request.GET: {self.request.GET}")                # <QueryDict: {}>
        # print(f"self.request.GET.keys(): {self.request.GET.keys()}")  # dict_keys([])
        # print(f"self.request: {self.request}")                        # <WSGIRequest: GET '/chirp/4/moderate/'>
        # print(f"self.request.method: {self.request.method}")          # GET
        # print(f"self.request.META: {self.request.META}")              # A META dictionary - lots of stuff in it.
        # Get the Chirp:
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
    # Send user back to home page after a chirp is deleted.
    success_url = reverse_lazy('chirps:home')

    def test_func(self):
        # Get the Chirp:
        chirp = self.get_object()
        # Return True if chirp.author is request user:
        print(f"self.request.user: {self.request.user}")
        print(f"chirp.author: {chirp.author}")
        print(f"Requesting user is Chirp author: {self.request.user == chirp.author}")
        return self.request.user == chirp.author        
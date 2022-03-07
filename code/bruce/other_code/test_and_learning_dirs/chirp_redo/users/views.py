from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# CustomUser needs.
from .forms import CustomUserCreationForm
from users.models import CustomUser


class SignUpView(CreateView):
    """
    Inherits 'CreateView'. View used to Create a new 'CustomUser'.
    """
    # We don't need to specify 'CustomUser' here since 'CustomUserCreationForm' uses it as we directed with 'model = CustomUser'.
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class UserProfileView(DetailView):
    """
    Inherits 'DetailView'. Displays users' profile info, and users' Chirps.
    """
    model = CustomUser
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        # Django packages up a dictionary 'self.kwargs' which has the key "'username'" from "'<str:username>/'", and passes that to the class view.
        # The 'self.kwargs['username']' here matches the "'<str:username>/'" in users/urls.py.
        # It's the 'kwarg' passed through the url.
        # The 'username' in 'username=' is the kwarg inside 'CustomUser' (and the get_object_or_404).
        return get_object_or_404(CustomUser, username=self.kwargs['username'])


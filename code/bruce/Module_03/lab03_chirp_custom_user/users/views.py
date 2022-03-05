from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# CustomUser needs.
from .forms import CustomUserCreationForm
from users.models import CustomUser


class SignUpView(CreateView):
    """
    Inherits UserCreationForm. Create a new user.
    """
    form_class = CustomUserCreationForm
    # form_class = UserCreationForm
    template_name = 'signup.html'
    # Waits until the end of loading classes to try to resolve the url.
    success_url = reverse_lazy('login')


class UserProfileView(DetailView):
    """
    Inherits 'DetailView'. Displays users' profile info.
    """
    model = CustomUser
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        # The built-in get_object:
        # The 'self.kwargs['pk']' is the 'pk' passed through the url.
        # return get_object_or_404(self.model, pk=self.kwargs['pk'])

        # The 'kwargs['username']' here matches the "'<str:username>/'" in users/urls.py.
        # It's the 'kwarg' passed through the url.
        # The 'username' in 'username=' is the kwarg inside 'User' (and the get_object_or_404).
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
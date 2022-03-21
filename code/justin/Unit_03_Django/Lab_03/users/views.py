from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import get_object_or_404


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserProfileView(generic.DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(get_user_model(), username=self.kwargs['username'])
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(get_user_model(), username=self.kwargs['username'])
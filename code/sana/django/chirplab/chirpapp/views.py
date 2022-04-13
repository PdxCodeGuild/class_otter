from django.shortcuts import render, redirect
from .models import chirp
from .forms import ChirpForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# chirps = [{'name': 'sana', 'text': 'a chirp'},{'name' : 'bob', 'text': 'bob chirpping'}]


# @login_required
# def home(request):
#     context = {'chirps' : chirp.objects.all}
#     return render(request, 'chirpapp/home.html', context)

class ChirpListView(LoginRequiredMixin, ListView):
    model = chirp
    template_name = 'chirpapp/home.html'
    ordering = ['-datetime']

class ChirpPostView(LoginRequiredMixin, CreateView):
    model = chirp
    template_name = 'chirpapp/chirp.html'
    fields = ['text']
    sucess_url = '/'


def postchirp(request):
    if(request.method == 'POST'):
        form = ChirpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChirpForm()
    return render(request, 'chirpapp/chirp.html', {'form' :form})
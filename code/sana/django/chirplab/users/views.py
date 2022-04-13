from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'User Registered')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form' :form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
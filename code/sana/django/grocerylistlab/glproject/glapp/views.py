
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import GLapp

# Create your views here.
def index(request):
    print("request", request.POST)
    groitem = GLapp.objects.all()
    if request.method == 'POST':
        new_item = GLapp(
            name = request.POST['name'],
            description = request.POST['description'],
            # update = request.POST['update'],
            # add_date = request.POST['add_date'],
            # completion = request.POST['completion'],
        )
        new_item.save()
        return redirect('/')
    
    return render(request, 'index.html', {'grolist' : groitem})

def delete(request, pk):
    groitem = GLapp.objects.get(id=pk)
    groitem.delete()
    return redirect('/')

def completed(request, pk):
    groitem = GLapp.objects.get(id=pk)
    groitem.completion = not groitem.completion
    groitem.save()
    return redirect('/')
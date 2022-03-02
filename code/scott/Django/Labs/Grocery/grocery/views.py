from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse 
from django.utils import timezone

from .models import GroceryItem

def index(request):
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocery/index.html', context)

def add(request):
    content = request.POST['content']
    GroceryItem.objects.create(content=content, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed = False if item.completed else True
    item.completed_date = timezone.now() if item.completed else None
    item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))

# def deleteGrocery_ListView(request, i):
#     y = Grocery_ListItem.objects.get(id= i)
#     y.delete()
#     return HttpResponseRedirect('/grocery_list_app/')


# Create your views here.

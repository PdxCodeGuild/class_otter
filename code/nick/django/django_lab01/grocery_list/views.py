from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import GroceryItem
from django.utils import timezone
from django.urls import reverse
# Create your views here.
def index(request):
    completed_items = GroceryItem.objects.filter(completed=True)
    incompleted_items = GroceryItem.objects.filter(completed=False)
    context = {
        'completed_items':completed_items,
        'incompleted_items': incompleted_items
    }
    return render(request, 'grocery_list/index.html', context)

def new(request):
    description = request.POST['description']    
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.completed:
        item.completed = False
        item.completed_date = None
    else:
        item.completed = True
        item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))
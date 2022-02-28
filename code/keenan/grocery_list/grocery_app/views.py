from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
# reverse lookup
from django.urls import reverse


from .models import GroceryItem


# Create your views here.
def index(request):
    item_list = GroceryItem.objects.all()
    # do not have a completed_date aspect to sort by
    completed_items = GroceryItem.objects.filter(completed_field=True).order_by('completed_date')
    incomplete_items = GroceryItem.objects.filter(completed_field=False).order_by('-completed_date')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocery_app/list.html', context)


# this creates a new grocery item 
def new(request):
    # the post was description before
    
    description = request.POST['item.item_text']
    # can use item = Grocery item ....
    # then do the .save
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed_field=False)
    return HttpResponseRedirect(reverse('grocery_list:list'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    # if item.completed:
    #     item.completed = False
    #     item.completed_date = None
    # else:
    #     item.completed = True
    #     item.completed_date = timezone.now()
    item.completed_field = False if item.completed_field else True
    item.completed_date = timezone.now() if item.completed_field else None
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:list'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:list'))
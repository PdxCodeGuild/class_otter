from django.shortcuts import get_object_or_404, render, get_list_or_404, reverse

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from .models import GroceryItem
from django.urls import reverse
from django.utils import timezone

def index(request):
    latest_grocery_list = GroceryItem.objects.filter(post_date__lte=timezone.now())
    completed_items = latest_grocery_list.filter(is_completed=True)
    not_completed = latest_grocery_list.filter(is_completed=False)
    context = {'latest_grocery_list': latest_grocery_list, 'not_completed': not_completed, 'completed_items': completed_items}
    return render(request, 'glist/index.html', context)

def create_item(request):
    description = request.POST['description']
    GroceryItem.objects.create(grocery_item=description, post_date=timezone.now())
    return HttpResponseRedirect(reverse('glist:index'))

def mark_complete(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    if grocery_item.is_completed == True:
        grocery_item.is_completed = False
    
    else:
        grocery_item.is_completed = True

    grocery_item.save()
    return HttpResponseRedirect(reverse('glist:index'))

def delete_item(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('glist:index'))
from webbrowser import get
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
   new_grocery_list = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
   context = {"new_grocery_list": new_grocery_list}
   return render(request,'grocery/index.html', context)

def add_item_to_list(request):
    ''' This creates items to list from user input'''
    grocery_item_description = request.POST['input_grocery_item']
    print(grocery_item_description)
    # line 18 creates item and saves to the data base.. text_description matches text_description in model
    g = GroceryItem.objects.create(text_description=grocery_item_description)
    print(f"this is an item {g}")
    # g.save()
    return HttpResponseRedirect(reverse('grocery:index'))



def mark_complete(request,pk):
    completed_list = []
    if request.method == 'POST':

        GroceryItem.objects.create(item_complete=request.POST['mark_complete'])
        grocery_item = get_object_or_404(GroceryItem, pk=pk)
        grocery_item.is_completed = False if grocery_item.is_completed else True 
        grocery_item.save()
    '''this will mark if task is complete'''
    grocery_checked_completed = request.POST['check_complete']
    print(grocery_checked_completed)
    c = GroceryItem.objects.check(is_completed=grocery_checked_completed)
    print(f"this item is completed {c}")
    completed_list.append(grocery_checked_completed)

    return HttpResponseRedirect(reverse('grocery:index'))


def delete(request, pk):
    grocery_item = get_object_or_404(GroceryItem,pk=pk)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect 
# from django.urls import reverse
# from django.utils import timezone

from .models import Grocery_ListItem

def grocery_list_appView(request):
    all_grocery_list_items = Grocery_ListItem.objects.all() # variable to store all the Grocery List items. 
    context = {'all_items': all_grocery_list_items}
    return render(request, 'grocery_list/grocery_list.html', context) #return context via Dict

def addGrocery_ListView(request):
    x = request.POST['content']
    new_item = Grocery_ListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/grocery_list_app/')
 

def deleteGrocery_ListView(request, i):
    y = Grocery_ListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/grocery_list_app/')

  
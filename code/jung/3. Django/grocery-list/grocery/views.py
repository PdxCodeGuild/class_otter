from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem
 

def index(request):
    grocery_list = GroceryItem.objects.filter(
        created_date__lte = timezone.now()
    ).order_by("-created_date")
    
    completed_item = grocery_list.filter(whether_it_was_completed_or_not = True)
    incompleted_item = grocery_list.filter(whether_it_was_completed_or_not = False)
    context = {"grocery_list": grocery_list, "completed_item": completed_item, "incompleted_item": incompleted_item}
    return render(request, 'grocery/index.html', context)

def create(request):
    text_description = request.POST['text_description']
    GroceryItem.objects.create(text_description = text_description, created_date = timezone.now(), whether_it_was_completed_or_not = False)
    return HttpResponseRedirect(reverse("grocery:index"))
    

def mark_complete(request, pk):
    
    item = get_object_or_404(GroceryItem, pk = pk)
    if item.whether_it_was_completed_or_not == True:
        item.whether_it_was_completed_or_not = False
        item.completed_date = None
    else:
        item.whether_it_was_completed_or_not = True
        item.completed_date = timezone.now()
    item.save()
    
    return HttpResponseRedirect(reverse("grocery:index"))


def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk = pk)
    item.delete()
    return HttpResponseRedirect(reverse("grocery:index"))


from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
# reverse lookup
from django.urls import reverse


from .models import GroceryItem


# Create your views here.
def index(request):
    item_list = GroceryItem.objects.all()
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by(-'completed_date')
    context = {'item_list': item_list}
    return render(request, 'grocery_app/list.html', context)


# this creates a new grocery item 
def new(request):
    description = request.POST['description']
    # can use item = Grocery item ....
    # then do the .save
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery:index'))

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import GroceryItem
from django.urls import reverse
from django.utils import timezone
# Create your views here.
def index(request):
    completed_items = GroceryItem.objects.filter(completed=True)
    incompleted_items = GroceryItem.objects.filter(completed_items=False)
    context = {'completed_items': completed_items, 'incompleted_items': incompleted_items}
    return render(request, 'grocery/index.html',context)

def new(request):
    description = request.POST['description']
    GroceryItem.objects.create(description=description, create_date = timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery:index'))
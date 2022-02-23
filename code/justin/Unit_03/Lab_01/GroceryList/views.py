from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import GroceryItem


class IndexView(generic.ListView):
    template_name = 'GroceryList/index.html'
    context_object_name = 'grocery_item_list'

    def get_queryset(self):
        return GroceryItem.objects.all().order_by('created_at')

def create(request):
    # request.POST['description']
    return HttpResponseRedirect(reverse('GroceryList:index'))

def update(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    is_completed = request.POST['item_completed']
    if is_completed == "True":
        item.completed_at = timezone.now()
    else:
        item.completed_at = None

    item.save()
    return HttpResponseRedirect(reverse('GroceryList:index'))

def delete(request, item_id):
    # item = get_object_or_404(GroceryItem, pk=item_id)
    return HttpResponseRedirect(reverse('GroceryList:index'))
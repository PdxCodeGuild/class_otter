from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic


from .models import GroceryItem

# View items in grocery list.
# Have form to add new grocery items to list.
# Handle marking GroceryItem.complete - True.
# Handle marking GroceryItem.complete - False.
# Handle deleting grocery items.


# def index(request):
#     print(request.POST)
#     print(request.POST.keys())

#     list_of_groceries = GroceryItem.objects.all().order_by('completed')

#     context = {'list_of_groceries': list_of_groceries}
#     return render(request, 'grocery_list/index.html', context)


class IndexView(generic.ListView):
    template_name = 'grocery_list/index.html'
    context_object_name = 'list_of_groceries'

    def get_queryset(self):
        """
        Get the list of groceries.
        """
        list_of_groceries = GroceryItem.objects.all().order_by('completed')
        return list_of_groceries


# Helper function to remove csrf token:
def remove_csrf_token(the_request):
    # Get the QueryDict:
    request = the_request.POST
    # Make a copy of QueryDict:
    mutible_item_dictionary = request.copy()
    mutible_item_dictionary.pop('csrfmiddlewaretoken')
    return mutible_item_dictionary


def complete(request):
    # # Get the QueryDict:
    # request = request.POST
    # # Make a copy of QueryDict:
    # mutible_item_dictionary = request.copy()
    # # print(f"mutible_item_dictionary: {mutible_item_dictionary}")
    # # Remove the csrf token: csrfmiddlewaretoken
    # # 'mutible_item_dictionary' will be a dictionary of items to mark completed.
    # mutible_item_dictionary.pop('csrfmiddlewaretoken')
    # # print(f"mutible_item_dictionary: {mutible_item_dictionary}")

    mutible_item_dictionary = remove_csrf_token(request)
    print(f"mutible_item_dictionary: {mutible_item_dictionary}")

    # Get keys for items to mark 'completed':
    # These 'keys' are strings so need to be typed 'int' to compare to 'int's in keys_for_all_items.
    keys_to_complete = [int(key) for key in mutible_item_dictionary.keys()]
    print(f"keys_to_complete: {keys_to_complete}")

    # I think we need all the pk's from database to compare with ones 'check'ed from request.POST.
    # WOW!!! This gets a 'list' of all the keys for the items in the database!
    keys_for_all_items = [item.pk for item in GroceryItem.objects.all()]
    print(f"keys_for_all_items: {keys_for_all_items}")
    
    # Loop through the grocery list:
    for pk in keys_for_all_items:
        # Get the item:
        item = get_object_or_404(GroceryItem, pk=pk)
        # If item 'checked' in form:
        if pk in keys_to_complete:
            # 'complete' the item:
            item.complete_item()
        else:
            # 'uncomplete' the item:
            item.uncomplete_item()
        # Save the state of the item:
        item.save()

    # If 'checked': 'complete_item():
        # Key will be in request object.

    # If not 'checked': 'uncomplete_item:
        # Key will not be in request object.

    return HttpResponseRedirect(reverse('grocery_list:index'))

def add(request):
    print(request.POST.keys())
    return HttpResponseRedirect(reverse('grocery_list:index'))
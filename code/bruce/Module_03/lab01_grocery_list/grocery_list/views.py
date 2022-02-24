from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic


from .models import GroceryItem


class IndexView(generic.ListView):
    template_name = 'grocery_list/index.html'
    context_object_name = 'uncompleted_groceries'
    
    # This has limited usage, only runs on server startup so only good for static files.
    # extra_context = {'text': [<>, <>]}

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are adding more 'context' attributes.
        print(context)
        print(context.keys())
        context['completed_groceries'] = GroceryItem.objects.filter(deleted = False, completed = True)
        print(context)
        print(context.keys())
        context['deletable_groceries'] = GroceryItem.objects.filter(deleted = False)
                # context[] = <another item>
        return context

    def get_queryset(self):
        """
        Get the list of groceries.
        """
        return GroceryItem.objects.filter(deleted = False, completed = False)


def add(request):
    """
    Adds a grocery item to the list.

    Function based view.
    """
    # Get the 'description' of the item to add:
    item_description_to_add = request.POST['description']

    # If 'item_description_to_add' is not empty string, add that 'description'
    # as new grocery item:
    if item_description_to_add != '':
        # Create an grocery item from the 'description':
        GroceryItem.objects.create(description=item_description_to_add)
    else:
        print("No item added.")

    return HttpResponseRedirect(reverse('grocery_list:index'))


# Helper function to remove csrf token:
def remove_csrf_token(the_request):
    """
    Removes the csrf token from QueryDict for further logic processing.
    """
    # Get the QueryDict:
    request = the_request.POST
    # Make a copy of QueryDict:
    mutible_item_dictionary = request.copy()
    # If 'csrfmiddlewaretoken' is present, remove it.
    if 'csrfmiddlewaretoken' in mutible_item_dictionary.keys():
        mutible_item_dictionary.pop('csrfmiddlewaretoken')
    # Return the dictionary which no longer contains the csrf token.
    return mutible_item_dictionary


# def complete(request, pk):
def complete(request):
    """
    Marks 'checked' grocery items as completed.
    """
    # Remove csrf token from request object:
    mutible_item_dictionary = remove_csrf_token(request)
    # print(f"mutible_item_dictionary: {mutible_item_dictionary}")

    # Create a list of keys for 'check'ed items, these will be 'complete'd:
    keys_to_complete = [key for key in mutible_item_dictionary.keys()]
    # print(f"keys_to_complete: {keys_to_complete}")

    # Loop through the grocery list:
    for pk in keys_to_complete:
        # Get the item:
        item = get_object_or_404(GroceryItem, pk=pk)
        # 'complete' the item:
        item.complete_item()
        print(f"Complete Item: {item}")
        # Save the state of the item:
        item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def uncomplete(request):
    """
    Marks the 'checked' grocery items as umcompleted.
    """
    # Remove csrf token from request object:
    mutible_item_dictionary = remove_csrf_token(request)
    # Create a list of keys for 'check'ed items, these will be un'complete'd:
    keys_to_uncomplete = [int(key) for key in mutible_item_dictionary.keys()]

    # Loop through the grocery list:
    for pk in keys_to_uncomplete:
        # Get the item:
        item = get_object_or_404(GroceryItem, pk=pk)
        # 'uncomplete' the item:
        item.uncomplete_item()
        # print(f"Uncomplete Item: {item}")
        # Save the state of the item:
        item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete(request):
    """
    Deletes a grocery item from the list.
    """
    # print(request.POST.keys())

    # Remove csrf token from request object:
    mutible_item_dictionary = remove_csrf_token(request)
    # print(f"mutible_item_dictionary: {mutible_item_dictionary}")

    # Get keys for items to 'delete':
    # These 'keys' are strings so need to be typed 'int' to compare to
    # 'int's in keys_for_all_items.
    keys_to_delete = [int(key) for key in mutible_item_dictionary.keys()]

    # Loop through the grocery list:
    for pk in keys_to_delete:
        # Get the item:
        item = get_object_or_404(GroceryItem, pk=pk)
        item.deleted = True
        item.save()
        # item.delete() # Old way, now we mark 'deleted' so it can be
        # recovered if necessary.

    return HttpResponseRedirect(reverse('grocery_list:index'))
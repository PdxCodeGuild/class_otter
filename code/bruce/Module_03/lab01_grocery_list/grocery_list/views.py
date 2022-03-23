from django.shortcuts import get_object_or_404
# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.utils import timezone
from django.views import generic


from .models import GroceryItem


class IndexView(generic.ListView):
    template_name = 'grocery_list/index.html'
    context_object_name = 'uncompleted_groceries'
    
    # This has limited usage, only runs on server startup so only good for static files.
    # The scope will be global since it's a class variable, in this case.
    # extra_context = {'text': [<>, <>]}

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are adding more 'context' attributes.
        # print(context)
        # print(context.keys())
        context['completed_groceries'] = GroceryItem.objects.filter(deleted = False, completed = True)
        # print(context)
        # print(context.keys())
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
    # Get the 'description', of the item to add, from the 'POST' 'request':
    item_description_to_add = request.POST['description']

    # If 'item_description_to_add' is not empty string, add that 'description'
    # as new grocery item:
    if item_description_to_add != '':
        # Create an grocery item from the 'description':
        grocery_item = GroceryItem.objects.create(description=item_description_to_add)
        print(f"Added Item: {grocery_item}")
    else:
        print("No item added.")

    return HttpResponseRedirect(reverse('grocery_list:index'))


# # Helper function to remove csrf token:
# def remove_csrf_token(the_request):
#     """
#     Removes the csrf token from QueryDict for further logic processing.
#     """
#     # Get the QueryDict:
#     request = the_request.POST
#     # Make a copy of QueryDict:
#     mutible_item_dictionary = request.copy()
#     # If 'csrfmiddlewaretoken' is present, remove it.
#     if 'csrfmiddlewaretoken' in mutible_item_dictionary.keys():
#         mutible_item_dictionary.pop('csrfmiddlewaretoken')
#     # Return the dictionary which no longer contains the csrf token.
#     return mutible_item_dictionary


# def complete(request):
def complete(request, pk):
    """
    Marks grocery items as completed.
    """
    # Get the item:
    item = get_object_or_404(GroceryItem, pk=pk)
    # 'complete' the item:
    item.complete_item()
    print(f"Completed Item: {item}")
    # Save the state of the item:
    item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def uncomplete(request, pk):
    """
    Marks grocery item as umcompleted.
    """
    # Get the item:
    item = get_object_or_404(GroceryItem, pk=pk)
    # 'uncomplete' the item:
    item.uncomplete_item()
    print(f"Uncompleted Item: {item}")
    # Save the state of the item:
    item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete(request, pk):
    """
    Deletes a grocery item from the list.
    """
    # Get the item for the provided pk:
    item = get_object_or_404(GroceryItem, pk=pk)
    # 'delete()' the item (set 'deleted' flag to True):
    item.delete()
    print(f"Deleted Item: {item}")
    # Save the state of the item:
    item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))
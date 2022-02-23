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


def add(request):
    """
    Adds a grocery item to the list.
    """
    # TODO: NOTE: There is a bug where clicking the 'Add item to list' button adds an empty item if there is no text in description block. <-- FIXED, I think. Added "if item_description_to_add != '':"
    # print(f"request.POST.keys(): {request.POST.keys()}")
    # # request.POST.keys(): dict_keys(['csrfmiddlewaretoken', 'description'])
    # Get the 'description' of the item to add:
    item_description_to_add = request.POST['description']
    # print(f"item_description_to_add: '{item_description_to_add}'")
    # print(f"type(item_description_to_add): {type(item_description_to_add)}")
    # print(f"len(item_description_to_add): {len(item_description_to_add)}")

    # Create an grocery item from the 'description':
    # # TODO: Understand these errors!
    # # NOTE: Needed to add the kwarg!
    # GroceryItem.objects.create(item_description_to_add)
    # # TypeError: QuerySet.create() takes 1 positional argument but 2 were given
    # g = GroceryItem(item_description_to_add)
    # g.save()
    # # ValueError: Field 'id' expected a number but got 'Geometric gravy'.

    # print(f"item_description_to_add == '': {item_description_to_add == ''}")
    if item_description_to_add != '':
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
    if 'csrfmiddlewaretoken' in mutible_item_dictionary.keys():
        mutible_item_dictionary.pop('csrfmiddlewaretoken')
    return mutible_item_dictionary


def complete(request):
    """
    Marks a grocery item completed.
    """
    # Remove csrf token from request object:
    mutible_item_dictionary = remove_csrf_token(request)
    # print(f"mutible_item_dictionary: {mutible_item_dictionary}")

    # Get keys for items to mark 'completed':
    # These 'keys' are strings so need to be typed 'int' to compare to 'int's in keys_for_all_items.
    keys_to_complete = [int(key) for key in mutible_item_dictionary.keys()]
    # print(f"keys_to_complete: {keys_to_complete}")

    # I think we need all the pk's from database to compare with ones 'check'ed from request.POST.
    # WOW!!! This gets a 'list' of all the keys for the items in the database!
    keys_for_all_items = [item.pk for item in GroceryItem.objects.all()]
    # print(f"keys_for_all_items: {keys_for_all_items}")
    
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
    # These 'keys' are strings so need to be typed 'int' to compare to 'int's in keys_for_all_items.
    keys_to_delete = [int(key) for key in mutible_item_dictionary.keys()]

    # Get pks for items in database:
    keys_for_all_items = [item.pk for item in GroceryItem.objects.all()]

    # Loop through the grocery list:
    for pk in keys_for_all_items:
        # Get the item:
        item = get_object_or_404(GroceryItem, pk=pk)
        # If item 'checked' to delete:
        if pk in keys_to_delete:
            # 'delete' the item:
            # print(f"Item to delete: {item}")
            item.delete()

    return HttpResponseRedirect(reverse('grocery_list:index'))
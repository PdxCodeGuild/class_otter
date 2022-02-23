import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

# Helper function to create a grocery item.
def new_grocery_item(grocery_item_description):
    return GroceryItem.objects.create(description=grocery_item_description)

class GroceryListModelTests(TestCase):

    def test_is_completed_false_for_new_grocery_item(self):
        """
        is_completed() returns False for a newly made, uncompleted, grocery item.
        """
        # Create a GroceryItem:
        grocery_item = GroceryItem(description="A grocery item")
        # Verify item is not completed (is_completed() == False):
        self.assertFalse(grocery_item.is_completed())
    
    def test_is_completed_true_for_grocery_item_completed(self):
        """
        is_completed() returns True for a grocery item with self.completed equals True.
        """
        # Create a GroceryItem:
        grocery_item = GroceryItem(description="A grocery item")
        # Set 'grocery_item.completed' to True:
        grocery_item.completed = True
        # Verify item is completed (is_completed() == True):
        self.assertTrue(grocery_item.is_completed())

    def test_complete_item(self):
        """
        complete_item() sets 'completed_date' to 'near' current time and 'completed' to True. 
        """
        # Create a GroceryItem:
        grocery_item = GroceryItem(description="A grocery item")
        # Complete the item:
        grocery_item.complete_item()
        # Verify grocery_item is completed:
        self.assertTrue(grocery_item.completed)
        # Verify grocery_item.completed_date 'near' (within ~1hour) now:
        self.assertLess(grocery_item.completed_date, timezone.now() + datetime.timedelta(days=.05))

    def test_uncomplete_item(self):
        """
        uncomplete_item() sets 'completed_date' to 'None' and 'completed' to False.
        """
        # Create GroceryItem:
        grocery_item = GroceryItem(description="A grocery item")
        # Complete the grocery_item:
        grocery_item.complete_item()
        # Verify 'grocery_item.completed' is True:
        self.assertTrue(grocery_item.completed)
        # Use the uncomplete_item() function:
        grocery_item.uncomplete_item()
        # Verify grocery_item is uncompleted:
        self.assertFalse(grocery_item.completed)
        # Verify 'grocery_item.completed_date' is 'None':
        self.assertIsNone(grocery_item.completed_date)
        

class IndexViewTests(TestCase):

    def test_no_grocery_items(self):
        """
        IndexView() returns 'No grocery items available.' with a 200 status when no grocery items are available.
        """
        # GET the response for 'grocery_list' 'index':
        response = self.client.get(reverse('grocery_list:index'))
        # Response should have status code of 200:
        # print(f"response.status_code: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        # Response should contain text 'No grocery items available.':
        self.assertContains(response, 'No grocery items available.')
    
    def test_one_grocery_item_present(self):
        """
        IndexView() returns a response which contains a grocery item.
        """
        # Create a grocery item:
        new_grocery_item('A New Grocery Item')
        # print(f"GroceryItem.objects.all(): {GroceryItem.objects.all()}")
        # GET the response from 'index' view:
        response = self.client.get(reverse('grocery_list:index'))
        # Response should contain the text 'A New Grocery Item':
        self.assertContains(response, 'A New Grocery Item')
        
    def test_two_grocery_items_present(self):
        """
        IndexView() returns a response which contains a grocery item.
        """
        # Create two grocery items:
        new_grocery_item('One New Grocery Item')
        new_grocery_item('Another New Grocery Item')
        # print(f"GroceryItem.objects.all(): {GroceryItem.objects.all()}")
        # GET the response from 'index' view:
        response = self.client.get(reverse('grocery_list:index'))
        # Response should contain the text 'One New Grocery Item':
        self.assertContains(response, 'One New Grocery Item')
        # Response should contain the text 'Another New Grocery Item':
        self.assertContains(response, 'Another New Grocery Item')

    # def test_item_shows_completed(self):
    #     """
    #     IndexView() returns a response which has an item's checkbox indicating it has been completed.
    #     """
    #     # Create grocery item:
    #     item = new_grocery_item('A New Grocery Item')
    #     # print(f"GroceryItem.objects.all(): {GroceryItem.objects.all()}")
    #     # GET the response from 'index' view:
    #     response = self.client.get(reverse('grocery_list:index'))
    #     # # Print the response content for visual testing:
    #     print(response.content)
    #     # # Figured out that the word 'checked' should not be present when no items are completed but 'checked' should be present when an item is 'completed'.
    #     # Response should not contain the text 'checked':
    #     self.assertNotContains(response, 'checked')
    #     print(item)
    #     print(f"item.completed: {item.completed}")
    #     # Complete the item:
    #     item.complete_item()
    #     print(item)
    #     print(f"item.completed: {item.completed}")
    #     # GET the response from 'index' view:
    #     response = self.client.get(reverse('grocery_list:index'))
    #     # print(response.content)
    #     # Response should contain the text 'checked':
    #     # self.assertContains(response, 'checked')

    #     # self.assertContains(response, 'h1')

    def test_completed(self):
        item = new_grocery_item("A grocery item")
        response = self.client.get(reverse('grocery_list:index'))
        # print(response.content)
        print(f"item: {item}")
        # item: 1: A grocery item - Completed[False]
        # print(f"item.completed: {item.completed}")
        # item.completed: False
        print(f"execute: 'item.complete_item()'")
        item.complete_item()
        response = self.client.get(reverse('grocery_list:index'))
        # print(response.content)
        print(f"item: {item}")
        # item: 1: A grocery item - Completed[True]
        # print(f"item.completed: {item.completed}")
        # item.completed: True

# From tests.py:
# <input type="checkbox" name="1" id="1" value="1" >
# From browser:
# <input type="checkbox" name="2" id="2" value="2" checked>

    def test_add_view(self):
        """
        add() adds item to list and redirects user to 'index' where item is displayed.
        """
        # Create dictionary to submit with POST request:
        grocery_item_to_add = {'description': "A grocery item"}
        # Submit the POST request:
        self.client.post(reverse('grocery_list:add'), grocery_item_to_add)
        # GET the response:
        response = self.client.get(reverse('grocery_list:index'))
        # Verify item 'A grocery item' shows up in 'response':
        self.assertContains(response, "A grocery item")



    def test_delete_view(self):
        """
        delete() deletes item from list and returns user to 'index' view where the item is no longer displayed.
        """
        # Create dictionary to submit with POST request:
        grocery_item_to_add = {'description': "A grocery item"}
        # Submit the POST request:
        self.client.post(reverse('grocery_list:add'), grocery_item_to_add)
        # GET the response:
        response = self.client.get(reverse('grocery_list:index'))
        # Verify item 'A grocery item' shows up in 'response':
        self.assertContains(response, "A grocery item")
        # Delete the grocery item:
        grocery_item_to_delete = {'1': 1}
        self.client.post(reverse('grocery_list:delete'), grocery_item_to_delete)
        # GET the response:
        response = self.client.get(reverse('grocery_list:index'))
        # Response should contain text 'No grocery items available.':
        self.assertContains(response, 'No grocery items available.')

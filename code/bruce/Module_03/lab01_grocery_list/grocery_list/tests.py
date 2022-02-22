import datetime

from django.test import TestCase
from django.utils import timezone

from .models import GroceryItem

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
        


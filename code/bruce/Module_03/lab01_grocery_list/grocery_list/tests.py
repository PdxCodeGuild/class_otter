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
        # This next test is, technically, not needed since it was tested above.
        # TODO: Decide if 'self.assertFalse(grocery_item.is_completed())' should be removed.
        # Verify item is not completed (is_completed() == False):
        self.assertFalse(grocery_item.is_completed())
        # Complete the GroceryItem:
        grocery_item.completed = True
        # print(f"grocery_item.completed:{grocery_item.completed} ?==? grocery_item.is_completed():{grocery_item.is_completed()}")
        # Verify item is completed (is_completed() == True):
        self.assertTrue(grocery_item.is_completed())

    def test_complete_item(self):
        """
        complete_item() sets 'completed_date' to current time and 'completed' to True. 
        """
        # Create a GroceryItem:
        grocery_item = GroceryItem(description="A grocery item")


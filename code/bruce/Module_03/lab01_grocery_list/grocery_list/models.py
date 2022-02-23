from django.db import models
from django.utils import timezone

#This can be done with a single app called grocery_list and model called GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.
# The user should be presented with an input field and a button (in a form). When the clicks the button, it should save the data to the server and show the newly-added item in the list. The user should be presented with a list of incomplete items and a list of complete items. THe user should be able to mark an item complete/incomplete and be able to delete an item.

class GroceryItem(models.Model):
    """
    Python class for grocery items in a grocery list.
    """
    description = models.CharField(max_length=200)

    created_date = models.DateTimeField('date created', auto_now_add=True)

    # Which is better for completed_date, 'null=True' or "default=''"?
    # NOTE: Need to use 'null=True' and set field to 'None' in python, then Django sets database field to 'NULL'.
    # completed_date = models.DateTimeField('date completed', default='') # <<-- Doesn't work!
    # Empty string '' is NOT DateTimeField type.

    # Resoures:
    # https://github.com/PdxCodeGuild/class_otter/blob/main/3%20Django/docs/06%20Models.md#nullable-fields

    # Can use 'self.completed_date = None' in 'uncomplete_item()'.
    completed_date = models.DateTimeField('date completed', null=True, blank=True)

    # 'completed' is a boolean. Database holds '0' for 'False' and '1' for 'True'.
    completed = models.BooleanField(default=False)

    # 'to_be_completed' - attribute used in 'complete' view to 'complete' items:
    to_be_completed = models.BooleanField(default=False)

    # 'to_be_uncompleted' - attribute used in 'complete' view to 'uncomplete' items:
    to_be_uncompleted = models.BooleanField(default=False)

    # Adding 'deleted' attribute here. May or may not use it.
    deleted = models.BooleanField(default=False)

    def __str__(self):
        '''The first triple-quote comment string.'''
        '''Added extra information to dunder string for use while building and debugging.'''
        return f"{self.id}: {self.description} - Completed[{self.completed}]"

    def is_completed(self):
        '''Check if item is completed.'''
        return self.completed

    def complete_item(self):
        '''Complete the item.'''
        self.completed_date = timezone.now()
        # 'completed' is a boolean. Database holds '0' for 'False' and '1' for 'True'.
        self.completed = True

    def uncomplete_item(self):
        '''Uncomplete the item.'''
        # Can set 'completed_date' to 'None' to 'uncomplete' the item.
        # This will set the database value to 'NULL'.
        self.completed_date = None
        # 'completed' is a boolean. Database holds '0' for 'False' and '1' for 'True'.
        self.completed = False        




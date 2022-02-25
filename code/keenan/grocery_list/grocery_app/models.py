import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.

class GroceryItem(models.Model):
    # the created date will be created when the item is added
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    completed_field = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_text

# Ask Merritt/Liz: action completed at 1107pm was showing as the next morning at 7:06am.  + 8 hours of time for admin page....
# adding and removing 'eggs' shows as the history for a single item, but it doesn't show the deleted action in the admin page
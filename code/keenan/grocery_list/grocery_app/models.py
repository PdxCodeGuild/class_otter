import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.

class GroceryItem(models.Model):
    # the created date will be created when the item is added
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField
    
    def __str__(self):
        return self.item_text
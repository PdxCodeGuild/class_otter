import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class GroceryItem(models.Model):
    # the created date will be created when the item is added
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    completed_field = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_text


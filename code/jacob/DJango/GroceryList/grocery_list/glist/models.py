from django.db import models
import datetime
from django.utils import timesince

# Create your models here.

class GroceryItem(models.Model):
    grocery_item = models.CharField(max_length=200)
    post_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.grocery_item


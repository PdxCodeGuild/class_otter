import datetime

from django.db import models
from django.utils import timezone


class Grocery_ListItem(models.Model):
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True) # to capture created date-time
    # complete = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content
# Create your models here.

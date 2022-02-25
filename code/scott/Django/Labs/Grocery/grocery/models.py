import datetime

from django.db import models


class GroceryItem(models.Model):
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True) # to capture created date-time
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content
# Create your models here.

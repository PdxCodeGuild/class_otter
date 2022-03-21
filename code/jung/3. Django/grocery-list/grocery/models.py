import datetime

from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    whether_it_was_completed_or_not = models.BooleanField(default=False)

    def __str__(self):
        return self.text_description


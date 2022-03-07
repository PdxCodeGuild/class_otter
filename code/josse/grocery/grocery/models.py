import datetime

from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text_description


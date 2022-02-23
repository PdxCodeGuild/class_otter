from django.conf import settings
from django.db import models


class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_completed(self):
        return (self.completed_at != None)

    def __str__(self):
        return self.description
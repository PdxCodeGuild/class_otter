from django.db import models


class GroceryItem(models.Model):

    item_create = models.CharField(max_length=50)
    create_item_date = models.DateTimeField(auto_now_add=True)
    complete_item_date = models.DateTimeField(null=True, blank=True)
    item_completed = models.BooleanField(default=False) 

    
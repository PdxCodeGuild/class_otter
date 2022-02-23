import datetime

from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
   text_description = models.CharField(max_length=200)
   pub_date = models.DateTimeField()

   def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


   def __str__(self):
        return self.text_description

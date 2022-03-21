from django.contrib import admin

# Register your models here.

from .models import GroceryItem

admin.site.register(GroceryItem)
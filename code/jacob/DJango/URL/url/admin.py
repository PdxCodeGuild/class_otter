from django.contrib import admin

# Register your models here.

from .models import Shortener

admin.site.register(Shortener)
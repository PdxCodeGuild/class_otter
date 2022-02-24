from django.conf import settings
from django.db import models


class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    short_code = models.CharField(max_length=16)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.short_code}=>{self.url}'

from django.conf import settings
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return f'{self.short_code}=>{self.url}'

    # link = models.ForeignKey(Link, related_name="clicks", on_delete=models.CASCADE)
    # language = models.CharField(max_length=256, blank=True, null=True)
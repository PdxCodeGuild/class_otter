from django.conf import settings
from django.db import models


class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    short_code = models.CharField(max_length=16)
    url = models.CharField(max_length=256)
    
    def __str__(self):
        return f'{self.short_code}=>{self.url}'

class Click(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.ForeignKey(Link, related_name="clicks", on_delete=models.CASCADE)
    referer = models.CharField(max_length=256, blank=True, null=True)
    remote_addr = models.GenericIPAddressField(blank=True, null=True, verbose_name=("remote address"))
    language = models.CharField(max_length=256, blank=True, null=True)
    user_agent = models.CharField(max_length=256, blank=True, null=True)
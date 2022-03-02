from django.conf import settings
from django.db import models


class Discussion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    message = models.CharField(max_length=128)


    def __str__(self):
        return f'{self.message[:16]}...'

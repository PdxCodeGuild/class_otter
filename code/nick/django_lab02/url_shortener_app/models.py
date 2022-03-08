from django.db import models

# Create your models here.
class UrlInfo(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.long_url} is {self.short_url}'
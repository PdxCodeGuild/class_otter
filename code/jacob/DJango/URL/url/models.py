from django.db import models

# Create your models here.

class Shortener(models.Model):
    url_to_shorten = models.CharField(max_length=200)
    url_short = models.CharField(max_length=6)

    def __str__(self):
        return self.url_to_shorten
from django.db import models

class UrlShortner(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=200)


    def __str__(self):
        return self.long_url

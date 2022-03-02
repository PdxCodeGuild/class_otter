from django.db import models

from .utils import create_shortened_url

class Urlshort(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
        # return f"Short Url for: {self.long_url} is {self.short_url}"
    
# The save method is being overwritten, which means you are introducing 
# new functionality to a pre-existing parent method. It is basically telling 
# Django that each time a “Shortener” object is saved and the short_url 
# isn’t specified, it must be filled with a random code. **This tip came from "Geekflare"***
    def save(self, *args, **kwargs):
        if not self.short_url:  # If the short url wasn't specified
            self.short_url = create_shortened_url(self)  # passes the model instance that is being saved

        super().save(*args, **kwargs)
        
        
# Create your models here.

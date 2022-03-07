from django.db import models

from datetime import datetime

from .utils import create_shortened_url

class Urlshort(models.Model):
    
#This model creates a short url from the user input long url: 
    # 'created' -  is the time and date the shortener was created
    #'times_followed' - collects the number of times the shortened link has been followed 
    # 'short_url' - sets certain parameters the shortened url will follow
    # 'long_url' is the original link supplied by the user
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)    
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    
    
    class Meta: #internal class Meta (allows for metadata options)

        ordering = ["-created"] #sets the option for ordering the Db for the project. In this case "Descending Order by Created Date."
                                # This is a tuple or list of strings and/or query expressions. 
                                # Each string is a field name with an optional “-” prefix, which indicates "descending order". 
                                # Fields without a leading “-” will be ordered ascending. Use the string “?” to order randomly.


    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
        # return f"Short Url for: {self.long_url} is {self.short_url}"
    
# The save method's functionality is changed (exteneded) so that each time a “Shortener” object is saved and the short_url 
# isn’t specified, it will be filled with random code. **This tip came from "Geekflare"***
# The save method is called to update the database with the shortened URL associated with the user's original URL.
    def save(self, *args, **kwargs):
        if not self.short_url:  # If the short url wasn't specified
            self.short_url = create_shortened_url(self)  # passes the model instance that is being saved

        super().save(*args, **kwargs)
        
        
# Create your models here.

from django.db import models

# Create your models here.

# when I go in to the admin page the title is 'Url items' for the database?
class UrlItem(models.Model):
    long_url = models.URLField(null=True, blank=True)
    short_url = models.CharField(max_length=6, unique=True, null=True)
    
    # can add  created = models.DateTimeField(auto_now_add=True)
    # times_followed = models.PositiveIntegerField(default=0) 
    # class Meta:  -- this sets that the ordering of shortener objects will be most recent first
    #       ordering = ["-created"]
    
    def __str__(self):
        # this could be return f'{self.long_url} to {self.short_url}' if we want to show what we did
        return self.long_url
from django.db import models

# Create your models here.

# when I go in to the admin page the title is 'Url items' for the database?
class UrlItem(models.Model):
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.description
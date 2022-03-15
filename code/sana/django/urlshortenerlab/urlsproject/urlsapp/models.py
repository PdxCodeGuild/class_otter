from django.db import models

# Create your models here.
class Link(models.Model):
    ulink = models.CharField(max_length=1000)
    slink = models.CharField(max_length=10)
    
    def __str__(self) :
        return self.name
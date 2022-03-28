from django.db import models
from django.contrib.auth import get_user_model

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    image_front = models.URLField(null=True, blank=True)
    image_back = models.URLField(null=True, blank=True)
    caught_by = models.ManyToManyField(get_user_model(), related_name='caught', null=True, blank=True) 

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')

    def __str__(self):
        return self.type
    

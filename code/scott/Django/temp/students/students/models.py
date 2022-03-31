from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=100)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher= models.CharField(max_length=50)
    capstone = models.URLField(max_length=200, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['-created']


# Create your models here.

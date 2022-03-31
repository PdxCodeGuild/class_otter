from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=100)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher= models.CharField(max_length=50)
    capstone = models.URLField(max_length=200, blank = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    



# Create your models here.
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
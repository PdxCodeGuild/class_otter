from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    favorite_topic = models.CharField(max_length=200)
    favorite_teacher = models.CharField(max_length=200)
    capstone = models.URLField



    def __str__(self):
        return self.first_name

    


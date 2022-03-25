from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cohort = models.CharField(max_length=30)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher = models.CharField(max_length=50)
    capstone = models.URLField(max_length=200)

    def __str__(self):
        return self.first_name
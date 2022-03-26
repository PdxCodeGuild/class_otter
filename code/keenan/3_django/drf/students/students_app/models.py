from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    favorite_topic = models.CharField(max_length=100)
    favorite_teacher = models.CharField(max_length=100)
    capstone = models.URLField()

    def __str__(self):
        return self.first_name

    #  could this work?
    #  def __str__(self):
    #     return self.first_name + self.last_name


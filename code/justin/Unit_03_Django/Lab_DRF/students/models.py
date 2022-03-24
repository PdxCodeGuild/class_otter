from django.db import models

class Student(models.Model):
    first_name = models.CharField(blank=False, max_length=256)
    last_name = models.CharField(blank=False, max_length=256)
    cohort = models.CharField(blank=False, max_length=256)
    favorite_topic = models.CharField(blank=True, max_length=256)
    favorite_teacher = models.CharField(blank=True, max_length=256)
    capstone = models.URLField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

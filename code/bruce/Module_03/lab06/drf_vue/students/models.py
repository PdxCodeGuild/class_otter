from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    favorite_topic = models.CharField(max_length=200)
    favorite_teacher = models.CharField(max_length=200)
    capstone = models.URLField('capstone url')
    students_app_url = models.URLField('students url', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-id']

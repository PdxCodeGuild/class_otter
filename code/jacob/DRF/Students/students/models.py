from django.db import models

class Student(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Cohort = models.CharField(max_length=100)
    FavoriteTopic = models.CharField(max_length=200)
    FavoriteTeacher = models.CharField(max_length=200)
    Capstone = models.URLField(max_length=200)

    def __str__(self):
        return self.FirstName

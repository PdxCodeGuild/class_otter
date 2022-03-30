from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    some_random_attribute = models.CharField(max_length=100, blank=True, null=True, default='')
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
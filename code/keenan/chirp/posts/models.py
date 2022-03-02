from django.db import models
from django.urls import reverse

# Posts models.py


class Post(models.Model):
    # similar to the posts / blog
    title = models.CharField(max_length=200, default='DEFAULT VALUE')
    # author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # body = models.TextField()

    def __str__(self):
        return self.title
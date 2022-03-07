from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('auth.user', related_name='chirps', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=280)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))
    
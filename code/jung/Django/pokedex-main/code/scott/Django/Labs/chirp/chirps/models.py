from django.db import models
from django.urls import reverse

# Create your models here.
class Chirp(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chirps:detail', args=(self.pk,))

    class Meta:
        ordering = ['-created']
from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    # title = models.CharField(max_length=200) # There isn't really a title for Chirps.
    author = models.ForeignKey('auth.User', related_name='chirps', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    tiny_body = models.TextField('Tiny Body', max_length=127)

    def __str__(self):
        return f"{self.author} : {self.tiny_body}"

    def get_absolute_url(self):
        return reverse('chirps:detail', args=(self.pk,))
    

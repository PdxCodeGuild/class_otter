from django.db import models
from django.urls import reverse
from chirp_project import settings

class Chirp(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chirps', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tiny_body = models.TextField('Tiny Body', max_length=127)

    def __str__(self):
        return f"{self.pk} : {self.author} : {self.tiny_body}"

    # This is used to specify the appropriate url representation of the Chirp. The url will be used when we 'create' or 'update' a Chirp.
    def get_absolute_url(self):
        # Two different ways to pass through the 'self.pk'.
        # return reverse('chirps:detail', args=(self.pk,))
        return reverse('chirps:detail', args=[self.pk])
    
    # Need this to order the Chirps on 'home' (ListView) page.
    class Meta:
        ordering = ['-created']
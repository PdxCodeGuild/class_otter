from django.db import models
from django.urls import reverse
from chirp_project import settings

class Chirp(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chirps', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # Using 'updated' here so we can track when Chirps are 'moderated'. Even though the 'Chirp's aren't typically 'updated'.
    updated = models.DateTimeField(auto_now=True)
    tiny_body = models.TextField('Tiny Body', max_length=127)

    def __str__(self):
        return f"{self.author} : {self.tiny_body}"

    # This is used to redirect user to the 'detail' page after they create a new Chirp.
    def get_absolute_url(self):
        return reverse('chirps:detail', args=(self.pk,))
    
    # Need this to order the Chirps on 'home' page.
    class Meta:
        ordering = ['-created']

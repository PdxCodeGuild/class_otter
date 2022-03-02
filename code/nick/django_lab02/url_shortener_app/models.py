from django.db import models

# Create your models here.
class Url(models.Model):
    short_url = models.CharField(max_length=5, unique=True, blank=True)
    long_url = models.URLField(null=True)

    def __str__(self):
        return self.long_url
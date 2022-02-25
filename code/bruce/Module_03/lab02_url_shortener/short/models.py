from django.db import models
from django.utils import timezone

class ShortCode(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.code} : {self.url}"


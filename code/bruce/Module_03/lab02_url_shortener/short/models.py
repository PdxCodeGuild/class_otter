from django.db import models
# from django.utils import timezone

class ShortCode(models.Model):
    url = models.URLField('long URL')
    url_description = models.CharField('URL description', max_length=200, null=True, blank=True)
    code = models.CharField('short code', max_length=200)
    created_date = models.DateTimeField('created date', auto_now_add=True)

    def __str__(self):
        return f"{self.pk} : {self.code} : {self.url_description}"


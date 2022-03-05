from django.db import models

# Create your models here.
class GLapp(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, max_length=500)
    update = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    completion = models.BooleanField(default=False)

    def __str__(self) :
        return self.name

from django.db import models

class Student(models.Model):

    first_name = models.CharField

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    
)

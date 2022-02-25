from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    completed_date = models.DateField(null=True, blank=True)
    completed =models.BooleanField()

    def __str__(self):
        return self.description
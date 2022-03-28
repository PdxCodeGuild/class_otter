from django.db import models

class GroceryItem(models.Model):

    description = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.description # The other variables above will follow.

# Terminal, run command, python manage.py makemigrations. Creates migration folder in grocery app.
# Run commnand, python manage.py migrate.
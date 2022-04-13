from django.db import models

# Create your models here.
    # First Name (CharField)
    # Last Name (CharField)
    # Cohort (CharField)
    # Favorite Topic (CharField)
    # Favorite Teacher (CharField)
    # Capstone (URLField)

class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    favorite_topic = models.CharField(max_length=200)
    favorite_teacher = models.CharField(max_length=200)
    capstone = models.URLField()

    def __str__(self):
        return self.first_name + self.last_name
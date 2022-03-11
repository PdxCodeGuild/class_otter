from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_moderator = models.BooleanField("moderator status", default=False, help_text="Designates whether a user should be treated as a moderator.")

    def __str__(self):
        return f"{self.pk}:{self.username} - Moderator:{self.is_moderator}"

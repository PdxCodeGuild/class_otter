from enum import unique
from urllib.request import AbstractBasicAuthHandler
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=24, null = True, blank= True)

    USERNAME_FIELD = 'nickname'

from email.mime import image
from django.db import models

class Feed(models.Model):
    profile_image = models.TextField()
    user_id = models.TextField()
    image = models.TextField()
    like_count = models.IntegerField()
    content = models.TextField()

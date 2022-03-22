from email.mime import image
from django.db import models

class Feed(models.Model):
    image = models.TextField()
    content = models.TextField()
    email = models.EmailField(default='')

class Like(models.Model): 
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)

class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()

class BookMark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)
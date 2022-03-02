from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    whistle = models.TextField(max_length=200)

    def __str__(self):
        return self.whistle

    
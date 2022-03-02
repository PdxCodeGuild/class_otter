from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    whistle = models.TextField(max_length=200)

    def __str__(self):
        return self.whistle

    class Meta:
        ordering = ['-created']   #'-' sorts in reverse order
    # def get_absolute_url(self):      ###this would require a detail page being created.
    #     return reverse("chirp:detail", args={"pk": self.pk})
    
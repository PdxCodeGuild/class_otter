from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS = (
    (0,'Draft'),
    (1,'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)

class Meta:
    ordering = ['-created_on']

def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))

def __str__(self):
    return self.title

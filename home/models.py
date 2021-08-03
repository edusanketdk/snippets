from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

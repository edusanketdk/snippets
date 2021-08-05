from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        print(self.slug)
        return reverse('blog_detail', kwargs={"slug": self.slug})
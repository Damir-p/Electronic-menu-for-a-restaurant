from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

from apps.menu.models import Category


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    body = RichTextField()
    upload_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('post_detail', args=[self.pk])


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    upload_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.post.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_link = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=50)
    body = RichTextField()

    def __str__(self):
        return self.name

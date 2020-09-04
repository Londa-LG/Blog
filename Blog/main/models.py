from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_description = models.TextField()
    thumbnail = models.ImageField()
    post = RichTextField()
    date_created = models.DateField()
    comment_count = models.IntegerField()
    view_count = models.IntegerField(default=0)
    category = models.ManyToManyField(Categories)
    featured = models.BooleanField(default=False)
    previous = models.ForeignKey('self', related_name='previous_post', on_delete=models.SET_NULL, blank=True, null=True)
    next = models.ForeignKey('self', related_name='next_post', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post', kwargs={'id': self.id})


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    comment = models.TextField()
    date_commented = models.DateField(auto_now_add=True)
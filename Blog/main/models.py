from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_description = models.TextField()
    thumbnail = models.ImageField()
    post = models.TextField()
    date_created = models.DateField()
    comment_count = models.IntegerField()
    category = models.ManyToManyField(Categories)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
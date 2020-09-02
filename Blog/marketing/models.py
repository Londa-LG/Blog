from django.db import models


class Signup(models.Model):
    email = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email



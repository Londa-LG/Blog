from django.contrib import admin
from .models import Categories, Post, Comments

admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Post)

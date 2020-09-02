from django.urls import path
from .views import Home, BlogPosts, Post

app_name= 'main'

urlpatterns = [
    path('', Home, name='home'),
    path('blog/', BlogPosts, name='blog'),
    path('post/', Post, name='post')
]

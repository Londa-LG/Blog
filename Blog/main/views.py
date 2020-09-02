from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def Home(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-date_created')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    content = {
        'featured': featured,
        'latest': latest
    }
    return render(request,'index.html',content)

def BlogPosts(request):
    return render(request,'blog.html')

def ViewedPost(request):
    return render(request,'post.html')
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q


from .models import Post
from .forms import CommentForm
from marketing.models import Signup

def Category_count():
    queryset = Post.objects.values('category__title').annotate(Count('category'))
    return queryset


def Search(request):
    post_list = Post.objects.all()
    query = request.GET.get('search')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(post_description__icontains=query) |
            Q(post__icontains=query)
        ).distinct()
    context ={
        'post_list': post_list
    }
    return render(request, 'search_results.html', context)


def Home(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-date_created')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'featured': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)

def BlogPosts(request):
    category_count = Category_count()
    posts = Post.objects.all()
    latest = Post.objects.order_by('-date_created')[0:3]
    paginator = Paginator(posts, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        pagination_qs = paginator.page(page)
    except PageNotAnInteger:
        pagination_qs = paginator.page(1)
    except EmptyPage:
        pagination_qs = paginator.page(paginator.num_pages)

    context = {
        'pagination': pagination_qs,
        'page_var': page_request_var,
        'latest': latest,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)

def ViewedPost(request,id):
    post = Post.objects.filter(id=id)
    category_count = Category_count()
    latest = Post.objects.order_by('-date_created')[0:3]
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.post = post
            form.save()
    context = {
        'latest': latest,
        'category_count': category_count,
        'post': post,
        'form': form,
    }
    return render(request, 'post.html', context)
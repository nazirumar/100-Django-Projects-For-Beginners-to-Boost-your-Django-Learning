from django.shortcuts import redirect, render
from django.contrib import messages
from newsapp.models import Blog
from newsapp.forms import BlogForm

# Create your views here.


def home(request):
    blogs=Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})


def blog_detail(request, pk):
    blog_query = ''
    return render(request, 'home.html', {'blog_query':blog_query})

def create_post(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form_user = form.save(commit=False)
                form_user.user = request.user
                form_user.save()
                messages.success(request, 'New post Was Added')
                return redirect('home')
    form = BlogForm()
    return render(request, 'blog_post.html', {'form':form})

def liked(request, pk):
    post_liked = Blog.objects.get(pk=pk)
    if not post_liked.liked:
        post_liked.liked = True
        post_liked.save()
        return redirect('home')
    else:
        post_liked.liked = False
        post_liked.save()
        messages.info(request, f'You Liked {post_liked.title}')
        return redirect('home')
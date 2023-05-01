from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from myapp.models import Topic, BlogPost, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import AuthenticationForm, RegistrationForm, NewBlogPostForm, NewCommentForm
from django.contrib.auth import login
from django.contrib.auth import logout


@login_required(login_url='/login/')
def blogs(request):
    topics = Topic.objects.all()
    if request.GET.get('blog_search'):
        blogs = BlogPost.objects.filter(title__icontains=request.GET.get('blog_search'))
    elif request.GET.get('topic_by_filter'):
        blogs = BlogPost.objects.filter(topics__title__icontains=request.GET.get('topic_by_filter'))
    else:
        blogs = BlogPost.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs, 'topics': topics})


@login_required(login_url='/login/')
def post(request, slug):
    post = BlogPost.objects.get(slug_url=slug)
    form = NewCommentForm()
    return render(request, 'post.html', {'post': post, 'form': form})


def add_comment(request, slug):
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            blog_post = BlogPost.objects.get(slug_url=slug)
            author = request.user
            new_comment = Comment(content=content,
                                  author=author,
                                  blog_post=blog_post)
            new_comment.save()
            return redirect('post', slug)
    else:
        return HttpResponseRedirect('/')


def about(request):
    return HttpResponse("надає звичайний текст для користувача, що описує функції сайту django.")


@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        form = NewBlogPostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            topics = request.POST.getlist('topics')
            print(f'eto topici {topics}')
            author = request.user
            new_blogpost = BlogPost(title=title,
                                    content=content,
                                    author=author)
            new_blogpost.save()
            for topic in topics:
                new_blogpost.topics.add(Topic.objects.get(title=topic))
            return HttpResponseRedirect('/')
    else:
        form = NewBlogPostForm()
    return render(request, 'create.html', {'form': form})


def update(request, slug):
    return HttpResponse(f"перегляд для оновлення наявних даних публікації.{slug}")


def delete(request, slug):
    return HttpResponse(f"перегляд для підтвердження видалення публікації {slug}")


def profile(request, username):
    return HttpResponse(f"Персональна сторінка користувача{username} ")


def change_password(request):
    return HttpResponse("Ця сторінка використовуватиметься для зміни облікових даних користувачів.")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username,
                                            last_name=last_name,
                                            first_name=first_name,
                                            password=password)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def my_logout(request):
    logout(request)
    return redirect("login")

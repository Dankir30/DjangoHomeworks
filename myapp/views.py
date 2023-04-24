from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic, BlogPost, Comment
from django.contrib.auth.models import User

def blogs(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})
def main(request):
    return render(request, 'base.html')


def post(request, slug):
    post = BlogPost.objects.get(slug_url=slug)
    return render(request, 'post.html', {'post': post})


def about(request):
    return HttpResponse("надає звичайний текст для користувача, що описує функції сайту django.")


def create(request):
    return render(request, 'create.html')


def add_comment(request, slug):
    return HttpResponse(
        f" це подання використовуватиметься для додавання коментарів до публікації блогу. Додано коментар {slug}")


def update(request, slug):
    return HttpResponse(f"перегляд для оновлення наявних даних публікації.{slug}")


def delete(request, slug):
    return HttpResponse(f"перегляд для підтвердження видалення публікації {slug}")


def profile(request, username):
    return HttpResponse(f"Персональна сторінка користувача{username} ")


def change_password(request):
    return HttpResponse("Ця сторінка використовуватиметься для зміни облікових даних користувачів.")


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("Логаут. Має перенаправляти користувача назад на домашню сторінку.")


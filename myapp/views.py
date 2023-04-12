from django.http import HttpResponse


def blogs(request):
    return HttpResponse("домашня сторінка сайту. Він міститиме список блогів, доступних на сайті django")


def post(request, slug):
    return HttpResponse(f"детальний перегляд окремої публікації в блозі. Публікація під ім'ям {slug}")


def about(request):
    return HttpResponse("надає звичайний текст для користувача, що описує функції сайту django.")


def create(request):
    return HttpResponse("форма створення публікації.")


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
    return HttpResponse("Сторінка з формою для реєстрації нового користувача.")


def login(request):
    return HttpResponse("Сторінка з формою для логіна.")


def logout(request):
    return HttpResponse("Логаут. Має перенаправляти користувача назад на домашню сторінку.")


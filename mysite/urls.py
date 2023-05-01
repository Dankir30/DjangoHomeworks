
from django.urls import path
from myapp.views import blogs, post, about, create, update, delete, profile, change_password, register,\
    my_login, my_logout
from django.contrib import admin

urlpatterns = [
    path("", blogs, name='blogs'),
    path('blogs/', blogs, name='blogs'),
    path("about/", about),
    path("create/", create, name='create'),
    path("<slug:slug>/update/", update),
    path("<slug:slug>/delete/", delete),
    path("profile/<str:username>/", profile, name='profile'),
    path("change_password/", change_password),
    path('register/', register, name='register'),
    path('login/', my_login, name='login'),
    path('logout/', my_logout, name='logout'),
    path('blog/<slug:slug>/', post, name='post'),
    path('admin/', admin.site.urls)
]

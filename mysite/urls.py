
from django.urls import path
from myapp.views import blogs, post, about, create, add_comment, update, delete, profile, change_password, register, login, logout


urlpatterns = [
    path("", blogs),
    path('blogs/', blogs),
    path("about/", about),
    path("<slug:slug>/comment/", add_comment),
    path("create/", create),
    path("<slug:slug>/update/", update),
    path("<slug:slug>/delete/", delete),
    path("profile/<str:username>/", profile),
    path("change_password/", change_password),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path("<slug:slug>/", post)


]

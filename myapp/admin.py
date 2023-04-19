from django.contrib import admin

from .models import Topic, BlogPost, Comment

admin.site.register(Topic)
admin.site.register(BlogPost)
admin.site.register(Comment)
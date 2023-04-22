from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    slug_url = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug_url = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'comment by {self.author.username}'


# user_dima = User.objects.get(id=2)
# user_me = User.objects.get(id=1)
# user_igor = User.objects.get(id=3)
# user_julia = User.objects.get(id=4)
# sport_topic = Topic.objects.create(title='sport', description='this topic is about all kinds of sport')
# sport_topic.users.add(user_julia)
# topic_movies = Topic.objects.create(title='movies', description='this topic is about movies')
# topic_movies.users.add(user_julia, user_me)
# post2 = BlogPost(title='I love BANANAS!', content='The banana is grown in the tropics, and, though it is most widely consumed in those regions, it is valued worldwide for its flavour, nutritional value, and availability througho
# ut the year. Cavendish, or dessert, bananas are most commonly eaten fresh, though they may be fried or mashed and chilled in pies or puddings. They may also be used to flavour muffins, cakes, or breads. ', author = User.objects.get(
# id=1))
# post2.save()
# post2.topics.add(Topic.objects.all()[0])
# comment1 = Comment(content='very good , very bad', author=User.objects.get(id=4), blog_post=BlogPost.objects.all()[0])
# comment1.save()
# comment2 = Comment(content='very good1 , very bad1', author=User.objects.get(id=3), blog_post=BlogPost.objects.all()[1])
# comment2.save()
# comment3 = Comment(content='very good2 , very bad2', author=User.objects.get(id=1), blog_post=BlogPost.objects.all()[2])
# comment3.save()
# comment4 = Comment(content='very good3 , very bad3', author=User.objects.get(id=1), blog_post=BlogPost.objects.all()[3])
# comment4.save()
# comment5 = Comment(content='very good4 , very bad4', author=User.objects.get(id=2), blog_post=BlogPost.objects.all()[1])
# comment5.save()
# comment6 = Comment(content='very good5 , very bad5', author=User.objects.get(id=2), blog_post=BlogPost.objects.all()[0])
# comment6.save()
# comment7 = Comment(content='very good6 , very bad6', author=User.objects.get(id=4), blog_post=BlogPost.objects.all()[3])
# comment7.save()
# post2 = BlogPost(title='Twitch is my live', content='i love streaming and eating ice cream', author=User.objects.get(id=4))
# post2.save()
# post2.topics.add(Topic.objects.all()[0])
# post2 = BlogPost(title='What is Cinderella is?', content='She was a young Greek courtesan who attracted the attention of the Pharaoh when an eagle flew off with her sandal, while she was taking a bath. The eagle dropped it in th
# e Pharaohs lap', author=User.objects.get(id=2))
# post2.save()
# post2.topics.add(Topic.objects.all()[1])
# post2 = BlogPost(title='Football is sucks', content='Its true, football is sucks', author=User.objects.get(id=1))
# post2.save()
# post2.topics.add(Topic.objects.all()[1])


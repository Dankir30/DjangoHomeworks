from django.contrib.auth import authenticate
from django import forms
from .models import Topic, BlogPost, Comment
from django.contrib.auth.models import User


class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=254)
    password = forms.CharField(label="Password:", widget=forms.PasswordInput, max_length=10)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('Incorrect')


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    username = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(label='Password:', max_length=15)

    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        print(type(username))
        users = User.objects.filter(username=username)
        print(type(users))
        if len(users):
            raise forms.ValidationError('Username exist')

    def clean_first_name(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("You can use only letters")

    def clean_last_name(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("You can use only letters")


class NewBlogPostForm(forms.Form):
    title = forms.CharField(label='Title: ', max_length=1000)
    content = forms.CharField(label='Text: ', widget=forms.Textarea)
    topics = forms.MultipleChoiceField(label='Topics:', choices=[(topic.title, topic.title) for topic in Topic.objects.all()], widget=forms.SelectMultiple)


class NewCommentForm(forms.Form):
    content = forms.CharField(label='New comment: ', widget=forms.Textarea, required=True)

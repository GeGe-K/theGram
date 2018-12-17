from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, 
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','birth_date','website','phone_number','profile_pic')


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'image')

from imagekit.models import ProcessedImageField
from django.db import models
import datetime as dt
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = HTMLField()
  website = models.CharField(max_length=30, blank=True)
  phone_number = models.IntegerField(blank=True, null=True)
  birth_date = models.DateField(null=True, blank=True)
  followers = models.ManyToManyField(
      'Profile', related_name='followers_profile', blank=True)
  following = models.ManyToManyField(
      'Profile', related_name='following_profile', blank=True)
  profile_pic = models.ImageField(
      upload_to='profile_pic/', null=True, blank=True)


# class Image(models.Model):
#     image_path = models.ImageField(upload_to='photos/')
#     name = models.CharField(max_length=40)
#     caption = models.TextField()


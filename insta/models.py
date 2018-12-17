from imagekit.models import ProcessedImageField
from django.db import models
import datetime as dt
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField

# Create your models here.

# class Image(models.Model):
#     image_path = models.ImageField(upload_to='photos/')
#     name = models.CharField(max_length=40)
#     caption = models.TextField()



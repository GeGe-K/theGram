from imagekit.models import ProcessedImageField
from django.db import models
import datetime as dt
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):

    '''
    Class contains user details.
    '''

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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()
    
    @classmethod
    def search_profile(cls, name):
        profile = cls.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(id = id)
        return profile


class Image(models.Model):

    '''
    Class contains image details
    '''
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    caption = HTMLField()
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null='True')

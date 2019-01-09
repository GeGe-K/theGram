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
    name = models.TextField(default='my name')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null='false', related_name='posts')
   

    def __str__(self):
      return self.name

    class Meta:
        ordering = ['-posted_on']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()

    @classmethod
    def get_images_on_profile(cls,profile):
      images = Image.objects.filter(profile__pk = profile)
      return images

    @property
    def count_comments(self):
      comments = self.comments.count()
      return comments

    @property
    def count_likes(self):
      likes = self.likes.count()

    def like(self, photo):
        if self.mylikes.filter(photo=photo).count() == 0:
            Likes(photo=photo, user=self).save()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null='True')

    def __str__(self):
      return self.name

    class Meta:
        ordering = ['-posted_on']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_on_image(cls, id):
        the_comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return self.comment


class Likes(models.Model):
    user_liked = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')
    liked_post = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='likes')

    def save_like(self):
        self.save()

    def __str__(self):
        return self.user_liked

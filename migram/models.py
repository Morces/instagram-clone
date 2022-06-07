
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to = 'users/pictures', blank=True, null=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    followings = models.ManyToManyField(User, related_name='followings', blank=True)


    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='migram/photos', blank=True)
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    


class Reels(models.Model):
    reel = models.FileField(upload_to='migram/reel')
    likes = models.ManyToManyField(User, blank=True)

class Story(models.Model):
    story = models.ImageField(upload_to='migram/story')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)


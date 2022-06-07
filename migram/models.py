
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to = 'users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    followings = models.ManyToManyField(User, related_name='followings', blank=True)


    def __str__(self):
        return self.user.username

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='migram/photos', blank=True)
    title = models.CharField(max_length=60)
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.profile.user.username)




class Reels(models.Model):
    reel = models.FileField(upload_to='migram/reel')
    likes = models.ManyToManyField(User, blank=True)

class Story(models.Model):
    story = models.ImageField(upload_to='migram/story')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)


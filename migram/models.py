
from django.db import models
from users.models import Profile
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
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


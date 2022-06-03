from django.db import models
from users.models import Profile


# Create your models here.
class Image(models.Model):
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='migram/photos', blank=True)
    image_name = models.CharField(max_length=60)
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.image_name, self.profile.user.username)
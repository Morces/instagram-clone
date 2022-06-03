from django.utils import timezone
from django.db import models



# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
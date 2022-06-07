from django.contrib import admin
from migram.models import Post, Reels, Story,Profile, Follow,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Reels)
admin.site.register(Follow)
admin.site.register(Comment)




from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin 
# from django.contrib.auth.models import User
from migram.models import Post, Reels, Story,Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Reels)
# admin.site.register(User)



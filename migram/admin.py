from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
from migram.models import Post, Reels, Story,Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Reels)

# class PostAdmin(admin.ModelAdmin):
#     list_display=('__str__', 'title', 'image', 'created', 'modified')
#     readonly_fields=('created','modified')
#     list_editable=('title', 'image')
#     search_fields=('profile__user__email','profile__user__username','profile__user__first_name', 'profile__user__last_name', 'title')
#     list_filter=('created', 'modified', 'profile__user__is_active','profile__user__is_staff')



# # Register your models here.

# class ProfileAdmin(admin.ModelAdmin):
#     list_display=('pk', 'user', 'phone_number', 'website', 'picture')
#     list_display_links=('pk', 'user')
#     list_editable=('phone_number', 'website', 'picture')
#     search_fields=('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')
#     list_filter=('user__is_active', 'user__is_active', 'created', 'modified')
#     fieldsets=(
#         ('Profile', {'fields':(
#             ('user', 'picture'),
#         )}),
#         ('Extra info', {'fields':(
#             ('phone_number', 'website'),
#             ('bio'),
#         )}),
#         ('Metadata', {'fields':(
#             ('created', 'modified'),
#         )}),
#     )
#     readonly_fields=('created', 'modified')

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete=False
#     verbose_name='profiles'

# class UserAdmin(BaseUserAdmin):
#     inlines=(ProfileInline,)
#     list_display=('username', 'first_name', 'last_name','is_active','is_staff')


# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)

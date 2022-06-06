from django.contrib import admin

from migram.models import Post

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('__str__', 'title', 'image', 'created', 'modified')
    readonly_fields=('created','modified')
    list_editable=('title', 'image')
    search_fields=('profile__user__email','profile__user__username','profile__user__first_name', 'profile__user__last_name', 'title')
    list_filter=('created', 'modified', 'profile__user__is_active','profile__user__is_staff')
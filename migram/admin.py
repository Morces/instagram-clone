from django.contrib import admin

from migram.models import Image

# Register your models here.
admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('__str__', 'image_name', 'image', 'created', 'modified')
    readonly_fields=('created','modified')
    list_editable=('image_name', 'image')
    search_fields=('profile__user__email','profile__user__username','profile__user__first_name', 'profile__user__last_name', 'image_name')
    list_filter=('created', 'modified', 'profile__user__is_active','profile__user__is_staff')
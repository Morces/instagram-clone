from migram.models import Image
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields=('profile', 'image_name', 'image')
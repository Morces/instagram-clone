from migram.models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('profile', 'title', 'image')
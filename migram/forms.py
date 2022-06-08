from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Profile,Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class LogInForm(UserCreationForm):
#     email = forms.EmailField(max_length=255, help_text='Required! Type a Valid email address!')
#     class Meta:
#         model = User
#         fields = ('username', 'password')


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=255, help_text='Required! Type a Valid email address!')

    class Meta:
        model = User
        fields= ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'location', 'picture', 'bio')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget=forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder']='Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)


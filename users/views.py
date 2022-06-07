from django.shortcuts import redirect, render
from migram.models import Post

from users.models import Profile



# Create your views here.
def profile(request, id=None):
    if not request.user.is_authenticated:
        return redirect('Login')
    if id is not None:
        profile_id = Profile.objects.get(id=id)
        posts = Post.objects.filter(profile=profile_id)
        posts_num = posts.count()
        profile = Profile.objects.get(user=request.user)
        picture = profile.picture.url
    else:
        profile_id = Profile.objects.get(user=request.user)
        posts = Post.objects.filter(user=request.user)
        posts_num = posts.count()
        profile = Profile.objects.get(user=request.user)
        picture = profile.picture.url
    
    return render(request, 'users/profile.html', {'profile':profile_id, 'picture':picture, 'profile_of_user':True, 'posts':posts, 'posts_num':posts_num})
    
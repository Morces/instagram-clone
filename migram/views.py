from email import message
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from migram.forms import CommentForm, PostForm, SignUpForm, UpdateUserForm, UpdateUserProfileForm
from migram.models import Follow, Post, Reels, Story,Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.generic import RedirectView


def index(request):
    images = Post.objects.all()
    stories = Story.objects.filter(profile__followers=request.user)
    context = {'images':images, 'stories':stories}
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, pasword=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def profile(request):
    images=request.user.profile.posts.all()
    if request.method =='POST':
        user_form=UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    context={'user_form':user_form, 'prof_form':prof_form, 'images':images}        
    return render(request, 'profile.html', context)

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status= False
    context={'user_prof':user_prof, 'user_posts':user_posts, 'followers':followers, 'follow_status':follow_status}
    return render(request, 'user_profile.html', context)

def post_comment(request, id):
    image = get_object_or_404(Post, pk=id)
    is_liked = False
    if image.likes.filter(id=request.user.id):
        is_liked=True
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context={'image':image, 'form':form, 'is_liked':is_liked, 'total_likes':image.total_likes() }
    return render(request, 'single.html', context)

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id = self.kwargs.get('id') 
        obj = get_object_or_404(Post, pk=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
        return url_  


def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get('search_user')
        results = Profile.search_profile(name)
        message = f'name'
        context = {'results':results,'message':message}
        return render(request, 'search.html', context)
    else:
        message = "You haven't searched for any images"
    return render(request, 'search.html', {'message':message})


def follow(request,to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower = request.user.profile, followed= user_profile3)
        follow_s.save()
           
        return redirect('user_profile', user_profile3.user.username)

def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed = user_profile2)
        unfollow_d.delete()
        return redirect('user_profile', user_profile2.user.username)

def upload_post(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method =='POST':
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    return render(request, 'upload-post.html', {'users':users})

def upload_reel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile=Profile.objects.get(user=request.user)
    picture = profile.picture.url
    if request.method=='POST':
        reel = request.FILES['reel']
        reels = Reels.objects.create(reel=reel)
        if reels:
            messages.success(request, 'Reel Uploaded')
    return render(request, 'upload-reel.html', {'picture':picture})

def reels(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    picture = profile.picture.url
    reels = Reels.objects.all()
    return render(request, 'reels.html', {'reels':reels, 'picture':picture})


def like_reel(request,id):
    reel= Reels.objects.get(id=id)
    if request.user in reel.likes.all():
        reel.likes.remove(request.user)
    else:
        reel.likes.add(request.user)
    return redirect('reels')

def like_post(request,id):
    post = Post.objects.filter(id=id)
    if request.user in post[0].likes.all():
        post[0].likes.remove(request.user)
    else:
        post[0].likes.add(request.user)
    return redirect('index')

def upload_story(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    picture = profile.picture.url
    if request.method=='POST':
        story = request.FILES['story']
        profile = Profile.objects.get(user=request.user)
        story_upload = Story.objects.create(story=story,profile=profile)
        if story_upload:
            messages.success(request, 'Story uploaded')
    return render(request, 'upload-story.html', {'picture':picture})


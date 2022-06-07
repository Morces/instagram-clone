
# from django.views.generic import ListView, CreateView,DetailView
# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin
# from migram.forms import PostForm
# from .models import Post
# from django.utils import timezone



# Create your views here.
#class CreatePostView(LoginRequiredMixin, CreateView):
 #   template_name='migram/new.html'
 #   success_url='/'
    # context_object_name='form'
 #   form_class=PostForm
 #   queryset=Post.objects.all()

    # def form_valid(self,form):
    #     print(form.cleaned_data)
        # form.instance.profile = self.request.user.profile
        # form.save()
        # return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context['profile']=self.request.user.profile
    #     return context

# class PostFeedView(ListView):
#     template_name = 'migram/post_card.html'
#     model = Post
#     queryset=Post.objects.all().filter(created__lte=timezone.now())
#     ordering = ('-created')
#     # paginate_by = 4
#     context_object_name = 'posts'

# class PostDetailView(DetailView):
#     template_name='migram/detail.html'
#     # slug_field='id'
#     # slug_url_kwarg='post_id'
#     queryset=Post.objects.all().filter(created__lte=timezone.now())
#     ordering = ('-created')
#     # context_object_name='posts'

#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Post, id=id_)



from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from migram.models import Post, Reels, Story,Profile
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.filter(Q(profile__followers=request.user) & ~Q(likes=request.user))
    story = Story.objects.filter(profile__followers=request.user)

    context = {'posts':posts, 'stories':story}
    return render(request, 'index.html', context)

def login(request):
    if not request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')

def create_profile(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        picture = request.FILES['image']
        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user, picture=picture)
        if profile:
            messages.success(request, 'Profile Created Successfully. Login Now!')
            return redirect('login')
    return render(request, 'signup.html')

def profile(request, id=None):
    if not request.user.is_authenticated:
        return redirect('login')
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
    
    return render(request, 'profile.html', {'profile':profile_id, 'picture':picture, 'profile_of_user':True, 'posts':posts, 'posts_num':posts_num})

def search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    picture = profile.picture.url
    search = request.GET['username']
    profiles= Profile.objects.filter(user__username__icontains=search)
    context = {'profiles':profiles, 'username':search, 'picture':picture}
    return render(request, 'search.html', context)


def follow(request,id,username):
    profile = Profile.objects.get(id=id)
    login_profile = Profile.objects.get(user=request.user) 
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        login_profile.followings.remove(profile.user)
    else:
        profile.followers.add(request.user)
        login_profile.followings.add(profile.user)
    return redirect(f'/search?username={username}')


def upload_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    picture = profile.picture.url
    if request.method=='POST':
        post = request.FILES['post']
        profile = Profile.objects.get(user=request.user)
        posts = Post.objects.create(user=request.user, image=post, profile=profile)
        if posts:
            messages.success(request, 'Post Uploaded!')
    return render(request, 'upload-post.html', {'picture':picture})

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


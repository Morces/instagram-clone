
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

from migram.models import Post, Story,Profile


def index(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    posts = Post.objects.filter(Q(profile__followers=request.user) & ~Q(likes=request.user))
    story = Story.objects.filter(profile__followers=request.user)

    context = {'posts':posts, 'stories':story}
    return render(request, 'migram/index.html', context)



def profile(request, id=None):
    if not request.user.is_authenticated:
        return redirect('Login')
    if id is not None:
        profile_id = Profile.objects.get(id=id)
        posts = Post.objects.filter(profile=profile)
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

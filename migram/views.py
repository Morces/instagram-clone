from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,DetailView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from migram.forms import PostForm
from .models import Post



# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name='migram/new.html'
    success_url=reverse_lazy('migram:feed')
    context_object_name='form'
    form_class=PostForm

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['profile']=self.request.user.profile
        return context

class PostFeedView(ListView):
    template_name = 'migram/post_card.html'
    model = Post
    queryset=Post.objects.all()
    ordering = ('-created')
    # paginate_by = 4
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name='migram/detail.html'
    slug_field='id'
    slug_url_kwarg='post_id'
    queryset=Post.objects.all()
    context_object_name='detail'



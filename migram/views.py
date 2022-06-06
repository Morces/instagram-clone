import imp
from django.views.generic import ListView, CreateView,DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from migram.forms import PostForm
from .models import Post
from django.utils import timezone



# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name='migram/new.html'
    success_url='/'
    # context_object_name='form'
    form_class=PostForm
    queryset=Post.objects.all()

    def form_valid(self,form):
        print(form.cleaned_data)
        form.instance.profile = self.request.user
        return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context['profile']=self.request.user.profile
    #     return context

class PostFeedView(ListView):
    template_name = 'migram/post_card.html'
    model = Post
    queryset=Post.objects.all().filter(created__lte=timezone.now())
    ordering = ('-created')
    # paginate_by = 4
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name='migram/detail.html'
    # slug_field='id'
    # slug_url_kwarg='post_id'
    queryset=Post.objects.all().filter(created__lte=timezone.now())
    ordering = ('-created')
    # context_object_name='posts'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)





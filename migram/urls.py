from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostDetailView,PostFeedView,CreatePostView

app_name='migram'

urlpatterns = [
    path('', PostFeedView.as_view(), name='post_list'),
    path('new/', CreatePostView.as_view(), name='create_post'),
    path('migram.<int:post_id>/', login_required(PostDetailView.as_view()),name='detail'),

]



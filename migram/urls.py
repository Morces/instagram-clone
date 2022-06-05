from django.urls import path
from django.contrib.auth.decorators import login_required
from migram import views

urlpatterns = [
    path(route='', view=views.PostFeedView.as_view(), name='feed'),
    path(route='migram/new/', view=views.CreatePostView.as_view(), name='create_post'),
    path(route='migram.<int:post_id>/', view=login_required(views.PostDetailView.as_view()),name='detail'),

]



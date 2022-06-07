from django.urls import path
from django.contrib.auth import login, logout, authenticate

from . import views
# from .views import PostDetailView,PostFeedView,CreatePostView

app_name='migram'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', CreatePostView.as_view(), name='create_post'),
    # path('<int:id>/', PostDetailView.as_view(),name='post_detail'),
    path('profile/', views.profile, name='profile'),

]



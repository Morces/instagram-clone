from django.urls import path, include
from migram.views import PostLikeToggle
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('profile/<username>', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='profile'),
    path('post/<id>', views.post_comment, name='comment'),
    path('search/', views.search_profile, name='search'),
    path('uploadreel/', views.upload_reel, name='upload_reel'),
    path('uploadpost/', views.upload_post, name='upload_post'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('reels/', views.reels, name='reels'),
    path('uploadstory/', views.upload_story, name='upload_story'),
    path('likereel/<int:id>/', views.upload_post, name='like_reel'),
    path('like/', views.like_post, name='like_post'),
    path('follow/<to_follow>/', views.follow, name='follow'),
    path('unfollow/<to_unfollow>/', views.unfollow, name='unfollow'),
]



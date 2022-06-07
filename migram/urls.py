from django.contrib.auth import authenticate, login, logout
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('search/', views.search_profile, name='search'),
    path('uploadreel/', views.upload_reel, name='upload_reel'),
    path('uploadpost/', views.upload_post, name='upload_post'),
    path('reels/', views.reels, name='reels'),
    path('uploadstory/', views.upload_story, name='upload_story'),
    path('likereel/<int:id>/', views.upload_post, name='like_reel'),
    path('like/<int:id>/', views.like_post, name='like'),
    path('follow/<int:id>/<str:username>/', views.follow, name='follow'),
]



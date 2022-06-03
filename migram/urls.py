from django.urls import path
from django.contrib.auth.decorators import login_required
from migram import views

urlpatterns = [
    path(route='', view=login_required(views.PostFeedView.as_view()), name='feed')
]



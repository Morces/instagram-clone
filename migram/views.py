from django.views.generic import ListView
from django.shortcuts import render

from migram.models import Image



# Create your views here.
class PostFeedView(ListView):
    template_name = 'migram/feed.html'
    model = Image
    ordering = ('-created')
    paginate_by = 4
    context_object_name = 'migram'
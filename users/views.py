from django.shortcuts import render

from users.models import Profile



# Create your views here.
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'profile':profile})
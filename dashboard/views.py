from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from video.models import Video

@login_required
def index(request):
    videos = Video.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {'videos': videos})

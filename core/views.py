from django.shortcuts import render, redirect
from video.models import Video
from .forms import SignupForm, LoginForm
from django.contrib.auth import logout

def index(request):
    videos = Video.objects.all()
    return render(request, 'core/index.html', {'videos': videos})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login/')

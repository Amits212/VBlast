from django.shortcuts import render, get_object_or_404
from .models import Video, Category
from django.contrib.auth.decorators import login_required
from .forms import NewVideoForm, EditVideoForm


def videos(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    videos = Video.objects.all()

    if category_id:
        videos = videos.filter(category_id=category_id)

    if query:
        videos = videos.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'video/videos.html', {
        'videos': videos,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    related_videos = Video.objects.filter(category=video.category).exclude(pk=pk)[0:3]
    return render(request, 'video/detail.html', {'video': video, 'related_videos': related_videos})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = NewVideoForm()

    return render(request, 'video/form.html', {'form': form})

@login_required
def delete(request, pk):
    video = get_object_or_404(Video, pk=pk, created_by=request.user)
    video.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    if request.method == 'POST':
        form = EditVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = EditVideoForm()

    return render(request, 'video/form.html', {'form': form})


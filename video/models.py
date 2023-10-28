from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    video = models.FileField(upload_to="videos/", default='default_video.mp4')
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.CASCADE, default=1)
    created_by = models.ForeignKey(User, related_name='video', on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def increment_likes(self):
        if self.like:
            self.like += 1
            self.save()

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('my_videos/', views.index, name='index')
]
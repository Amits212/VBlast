from django.forms import ModelForm
from .models import Video
from django import forms

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewVideoForm(ModelForm):
    class Meta:
        model= Video
        fields= ['name','description','video']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'video': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class EditVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'description', 'video']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'video': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
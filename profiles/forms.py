# seu_app/forms.py

from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['path_image']
        widgets = {
            'path_image': forms.FileInput(attrs={'id': 'id_path_image', 'class': 'd-none'}),
        }
        labels = {
            'path_image': '',
        }

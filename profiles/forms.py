from django import forms
from .models import Photo, Address
from django.contrib.auth.models import User


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('path_image',)
        widgets = {
            'path_image': forms.FileInput(attrs={'id': 'id_path_image', 'class': 'd-none'}),
        }
        labels = {
            'path_image': '',
        }

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email',)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('user_address',)
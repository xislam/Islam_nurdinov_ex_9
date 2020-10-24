from django import forms
from webapp.models import PhotoGallery


class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = ['img', 'description', 'author_name']


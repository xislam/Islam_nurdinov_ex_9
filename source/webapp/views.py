from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from webapp.models import PhotoGallery


class IndexView(ListView):
    template_name = ''
    context_object_name = 'photos'
    model = PhotoGallery
    ordering = '-creation_date'


class PhotoGalleryView(DetailView):
    template_name = ''
    pk_url_kwarg = 'pk'
    model = PhotoGallery


class IndexView():
    pass


class IndexView():
    pass


class IndexView():
    pass

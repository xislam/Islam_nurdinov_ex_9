from abc import ABC
from audioop import reverse

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from webapp.forms import PhotoGalleryForm
from webapp.mixins import StatsMixin
from webapp.models import PhotoGallery


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'photos'
    model = PhotoGallery
    ordering = '-creation_date'


class PhotoGalleryView(DetailView):
    template_name = 'photo_detail.html'
    context_object_name = 'photo'
    model = PhotoGallery


class PhotoGalleryCreateView(LoginRequiredMixin, StatsMixin, CreateView):
    template_name = 'photo_c.html'
    model = PhotoGallery
    # form_class = PhotoGalleryForm
    fields = ['img', 'description']
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        form.instance.author_name = self.request.user
        return super().form_valid(form)


class PhotoGalleryUpdateView(UserPassesTestMixin, UpdateView, ABC):
    model = PhotoGallery
    template_name = 'photo_update.html'
    fields = ['img', 'description', 'author_name']
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        if self.request.user.has_perm('photoGallery_change') or self.get_object().author_name == self.request.user:
            return True


class PhotoGalleryDeleteView(UserPassesTestMixin, DeleteView, ABC):
    template_name = 'photo_delete.html'
    model = PhotoGallery
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        if self.request.user.has_perm('photoGallery_delete') or self.get_object().author_name == self.request.user:
            return True
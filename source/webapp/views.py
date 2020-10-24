from audioop import reverse

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from webapp.models import PhotoGallery


class IndexView(ListView):
    template_name = ''
    context_object_name = 'photos'
    model = PhotoGallery
    ordering = '-creation_date'


class PhotoGalleryView(DetailView):
    template_name = 'photo_detail.html'
    pk_url_kwarg = 'pk'
    model = PhotoGallery


class PhotoGalleryCreateView(CreateView):
    template_name = 'photo_create.html'
    model = PhotoGallery
    fields = ['image', 'description']

    def valid(self, form):
        form.instance.author_name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoGalleryUpdateView(UpdateView):
    model = PhotoGallery
    template_name = 'photo_update.html'
    fields = ['image', 'description', 'author_name']
    context_object_name = 'obj'

    def get(self):
        return reverse('webapp:index')


class PhotoGalleryDeleteView(DeleteView):
    template_name = 'photo_delete.html'
    model = PhotoGallery
    context_object_name = 'obj'
    success_url = reverse_lazy('webapp:index')

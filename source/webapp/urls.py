from django.urls import path
from webapp.views import IndexView, PhotoGalleryView, PhotoGalleryCreateView, PhotoGalleryUpdateView, \
    PhotoGalleryDeleteView


app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoGalleryView.as_view(), name='photo_gallery_view'),
    path('photo/add/', PhotoGalleryCreateView.as_view(), name='photo_gallery_create'),
    path('photo/<int:pk>/edit/', PhotoGalleryUpdateView.as_view(), name='photo_gallery_update'),
    path('photo/<int:pk>/delete/', PhotoGalleryDeleteView.as_view(), name='photo_gallery_delete'),

]

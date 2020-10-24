from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class PhotoGallery(models.Model):
    # user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    img = models.ImageField(null=False, blank=False, upload_to='media', verbose_name='Фото')
    description = models.TextField(null=False, blank=False, max_length=1000, verbose_name='Подпись')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author_name = models.CharField(null=False, blank=False, max_length=60, verbose_name='Автор')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='favorite',
                             on_delete=models.CASCADE)
    photo = models.ForeignKey('PhotoGallery', verbose_name='Фото', on_delete=models.CASCADE,
                              related_name='favorite_status')

    def __str__(self):
        return self.user
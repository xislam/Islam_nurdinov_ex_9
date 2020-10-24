from django.db import models


class PhotoGallery(models.Model):
    img = models.ImageField(null=False, blank=False, upload_to='media', verbose_name='Фото')
    description = models.TextField(null=False, blank=False, max_length=1000, verbose_name='Подпись')
    author_name = models.CharField(null=False, blank=False, max_length=60, verbose_name='Автор')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'



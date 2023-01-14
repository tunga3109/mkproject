from django.db import models
from django.urls import reverse


# class Part(models.Model):
#     version = models.CharField(
#         max_length=64,
#         unique=True,
#         verbose_name='Версия игры',
#         help_text='Макс. 64 символа'
#     )
#     slug = models.SlugField(verbose_name='URL', unique=True)
#
#     def __str__(self):
#         return self.version
#
#     class Meta:
#         verbose_name = 'часть'
#         verbose_name_plural = 'часть'
#         db_table = 'fighters_part'


class Fighter(models.Model):
    character_name = models.CharField(
        max_length=128,
        verbose_name='Имя героя'
    )
    descr = models.TextField(verbose_name='описание')
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )
    # version = models.ForeignKey(
    #     Part,
    #     on_delete=models.DO_NOTHING,
    #     verbose_name='категория'
    # )
    image = models.ImageField(
        upload_to='post',  # от папки media/ поэтому не прописываем media/post
        null=True,
        blank=True,
        verbose_name='картинка'
    )

    def __str__(self):
        return self.character_name

    def get_absolute_url(self):
        return reverse('fighter_post', kwargs={'fighter_slug': self.slug})

    class Meta:
        db_table = 'fighter_names'
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
        ordering = ['-character_name']

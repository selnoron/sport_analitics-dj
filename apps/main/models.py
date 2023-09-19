from django.db import models
from django.contrib.auth.models import User


class Sports(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=50
    )

    class Meta:
        verbose_name = 'спорт'
        verbose_name_plural = 'спорт'
        ordering = ('name',)
    
    def __str__(self) -> str:
        return self.name


class Matches(models.Model):
    sport_type = models.ForeignKey(
        verbose_name='игра',
        related_name='video_of_sport',
        to=Sports,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    video_file = models.FileField(
        verbose_name='видео файл',
        upload_to='video/%Y/%m/%d/'
    )

    def __str__(self) -> str:
        return self.sport_type.name
    
    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'видео'
        ordering = ('sport_type',)


class Favourite(models.Model):
    user = models.ForeignKey(
        verbose_name='кого',
        to=User,
        related_name='user_favourites',
        on_delete=models.CASCADE
    )

    matches = models.ForeignKey(
        verbose_name='какой матч',
        to=Matches,
        related_name='f_matches',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'избранные'
        verbose_name_plural = 'избранные'
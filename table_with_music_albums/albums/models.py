from django.db import models


class Artist(models.Model):
    name = models.CharField(unique=True, max_length=200,)

    class Meta:
        ordering = ['name']
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='album'
    )
    year = models.PositiveSmallIntegerField(verbose_name='Год')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'artist'], name='unique_album'
            )
        ]
        ordering = ['name']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.name+f'[{self.year}]'


class Track(models.Model):
    name = models.CharField(max_length=200, verbose_name='Композиция')
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE,
        verbose_name='Альбом',
        related_name='tracks'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'album'], name='unique_track'
            )
        ]
        ordering = ['name']
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'

    def __str__(self):
        return self.name

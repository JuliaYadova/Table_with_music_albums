from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения Альбома.
    tracks: переопределяется на метод __str__ по related_name
    album: вызывается метод объекта для отображения строкового метода объекта.
    extra_kwargs: по тЗ имя поля заменяется на указание вложения знаком @.

    """
    tracks = serializers.StringRelatedField(many=True, read_only=True)
    album = serializers.CharField(source='__str__')

    class Meta:
        model = Album
        fields = ('album',
                  'name',
                  'artist@name',
                  'tracks',)
        extra_kwargs = {
            'artist@name': {'source': 'get_artist', 'read_only': True},
        }

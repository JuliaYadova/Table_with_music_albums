from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import CustomOrderingFilterSet
from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filterset_class = CustomOrderingFilterSet
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ('name', 'artist')

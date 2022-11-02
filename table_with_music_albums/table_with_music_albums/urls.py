from django.contrib import admin
from django.urls import path

from albums.views import AlbumViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', AlbumViewSet.as_view({'get': 'list'}), name='index'),
]

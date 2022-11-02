from django.contrib import admin

from .models import Album, Artist, Track

admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Artist)

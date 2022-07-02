from django.contrib import admin

from django.contrib import admin
from .models import *


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'album', 'language', 'release_date', 'time', 'genre', 'photo')
    list_display_links = ('id', 'song_name')
    search_fields = ('song_name', 'genre')


admin.site.register(Song, MusicAdmin)

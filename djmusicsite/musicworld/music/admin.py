from django.contrib import admin

from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'album', 'language', 'release_date', 'time', 'genre', 'photo')
    list_display_links = ('id', 'song_name')
    search_fields = ('song_name', 'genre')


class SingerAdmin(admin.ModelAdmin):
    list_display = ('id', 'singer_firstname', 'singer_lastname', 'group', 'pseudonym', 'bio', 'photo')
    list_display_links = ('id', 'singer_lastname')
    search_fields = ('singer_lastname', 'pseudonym')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_firstname', 'author_lastname', 'bio', 'photo')
    list_display_links = ('id', 'author_lastname')


admin.site.register(Song, SongAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(Author, AuthorAdmin)
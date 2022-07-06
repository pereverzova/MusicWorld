from django.contrib import admin

from django.contrib import admin
from .models import *


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')
    list_display_links = ('id', 'genre_name')


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_name', 'album', 'language', 'release_date', 'time', 'genre', 'photo')
    list_display_links = ('id', 'song_name')
    search_fields = ('song_name', 'genre')


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'library_name')
    list_display_links = ('id', 'library_name')


class LibraryListAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'library')
    list_display_links = ('id', 'song')


class SingerAdmin(admin.ModelAdmin):
    list_display = ('id', 'singer_firstname', 'singer_lastname', 'group', 'pseudonym', 'bio', 'photo')
    list_display_links = ('id', 'singer_lastname')
    search_fields = ('singer_lastname', 'pseudonym')


class SingerListAdmin(admin.ModelAdmin):
    list_display = ('id', 'singer', 'song')
    list_display_links = ('id', 'song')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_firstname', 'author_lastname', 'bio', 'photo')
    list_display_links = ('id', 'author_lastname')


class AuthorListAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'song')
    list_display_links = ('id', 'song')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_nickname')
    list_display_links = ('id', 'user_nickname')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_grade', 'user', 'song')
    list_display_links = ('id', 'user')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(LibraryList, LibraryListAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(SingerList, SingerListAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorList, AuthorListAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Rating, RatingAdmin)
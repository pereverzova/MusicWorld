from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    songs = Song.objects.all()
    return render(request, 'music/index.html', {'songs': songs, 'title': 'Головна сторінка', 'genre_id': 0})


def song(request, song_id):
    song = Song.objects.get(id=song_id)
    authorlist = AuthorList.objects.filter(song_id=song_id)
    singerlist = SingerList.objects.filter(song_id=song_id)
    librarylist = LibraryList.objects.filter(song_id=song_id)
    return render(request, 'music/song.html', {'authorlist': authorlist, 'singerlist': singerlist, 'librarylist': librarylist, 'song': song, 'title': 'Пісня', 'song_id': song_id})


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    songlist = AuthorList.objects.filter(author_id=author_id)
    return render(request, 'music/author.html', {'songlist': songlist, 'author': author, 'title': 'Про автора', 'author_id':author_id})


def singer(request, singer_id):
    singer = Singer.objects.get(id=singer_id)
    songlist = SingerList.objects.filter(singer_id=singer_id)
    return render(request, 'music/singer.html', {'songlist': songlist, 'singer': singer, 'title': 'Про співака', 'singer_id':singer_id})


def library(request, library_id):
    library = Library.objects.get(id=library_id)
    songlist = LibraryList.objects.filter(library_id=library_id)
    return render(request, 'music/library.html', {'songlist': songlist, 'library': library, 'title': 'Про бібліотеку', 'genre_id':library_id})


def task(request):
    return render(request, 'music/task.html', {'title': 'Завдання', 'menu_selected':'task'})


def genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    songs = Song.objects.filter(genre_id=genre_id)
    return render(request, 'music/index.html', {'songs': songs, 'genre': genre, 'title': 'Жанр', 'genre_id':genre_id})


def authors(request):
    infoauthor = Author.objects.all()
    return render(request, 'music/authors.html', {'infoauthor': infoauthor, 'title': 'Автори', 'menu_selected':'authors'})


def singers(request):
    infosinger = Singer.objects.all()
    return render(request, 'music/singers.html', {'infosinger': infosinger, 'title': 'Співаки', 'menu_selected':'singers'})

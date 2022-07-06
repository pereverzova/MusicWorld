from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(request):
    songs = Song.objects.all()
    return render(request, 'music/index.html', {'songs': songs, 'title': 'MusicWorld', 'genre_id': 0})


def add(request):
    if request.method == 'POST':
        songform = SongForm(request.POST, request.FILES)
        if songform.is_valid():
            print(songform.cleaned_data)
            songform.save()
    else:
        songform = SongForm()

    if request.method == 'POST':
        authorform = AuthorForm(request.POST, request.FILES)
        if authorform.is_valid():
            print(authorform.cleaned_data)
            authorform.save()
    else:
        authorform = AuthorForm()

    if request.method == 'POST':
        authorlistform = AuthorListForm(request.POST)
        if authorlistform.is_valid():
            print(authorlistform.cleaned_data)
            authorlistform.save()
    else:
        authorlistform = AuthorListForm()

    if request.method == 'POST':
        singerform = SingerForm(request.POST, request.FILES)
        if singerform.is_valid():
            print(singerform.cleaned_data)
            singerform.save()
    else:
        singerform = SingerForm()

    if request.method == 'POST':
        singerlistform = SingerListForm(request.POST)
        if singerlistform.is_valid():
            print(singerlistform.cleaned_data)
            singerlistform.save()
    else:
        singerlistform = SingerListForm()

    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            print(userform.cleaned_data)
            userform.save()
    else:
        userform = UserForm()

    if request.method == 'POST':
        ratingform = RatingForm(request.POST)
        if ratingform.is_valid():
            print(ratingform.cleaned_data)
            ratingform.save()
    else:
        ratingform = RatingForm()

    if request.method == 'POST':
        libraryform = LibraryForm(request.POST)
        if libraryform.is_valid():
            print(libraryform.cleaned_data)
            libraryform.save()
    else:
        libraryform = LibraryForm()

    if request.method == 'POST':
        librarylistform = LibraryListForm(request.POST)
        if librarylistform.is_valid():
            print(librarylistform.cleaned_data)
            librarylistform.save()
    else:
        librarylistform = LibraryListForm()

    if request.method == 'POST':
        genreform = GenreForm(request.POST)
        if genreform.is_valid():
            print(genreform.cleaned_data)
            genreform.save()
    else:
        genreform = GenreForm()

    context = {
        'songform': songform,
        'authorform': authorform,
        'authorlistform': authorlistform,
        'singerform': singerform,
        'singerlistform':singerlistform,
        'userform':userform,
        'ratingform': ratingform,
        'libraryform': libraryform,
        'librarylistform': librarylistform,
        'genreform': genreform,
        'title': 'Додати інформацію',
        'menu_selected': 'add'
    }
    return render(request, 'music/add.html', context=context)


def song(request, song_id):
    song = Song.objects.get(id=song_id)
    authorlist = AuthorList.objects.filter(song_id=song_id)
    singerlist = SingerList.objects.filter(song_id=song_id)
    librarylist = LibraryList.objects.filter(song_id=song_id)
    rating = Rating.objects.filter(song_id=song_id)
    return render(request, 'music/song.html', {'authorlist': authorlist, 'singerlist': singerlist, 'librarylist': librarylist, 'rating' : rating, 'song': song, 'title': 'Пісня', 'song_id': song_id})


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
    return render(request, 'music/index.html', {'songs': songs, 'genre': genre, 'title': 'Пісні у жанрі '+ '"' + genre.genre_name + '"', 'genre_id':genre_id})


def authors(request):
    infoauthor = Author.objects.all()
    return render(request, 'music/authors.html', {'infoauthor': infoauthor, 'title': 'Автори', 'menu_selected':'authors'})


def singers(request):
    infosinger = Singer.objects.all()
    return render(request, 'music/singers.html', {'infosinger': infosinger, 'title': 'Співаки', 'menu_selected':'singers'})


def libraries(request):
    libraries = Library.objects.all()
    return render(request, 'music/libraries.html', {'libraries': libraries, 'title': 'Бібліотеки', 'menu_selected':'libraries'})


def rating(request):
    return render(request, 'music/rating.html', {'title': 'Рейтинг', 'menu_selected': 'rating'})


def authorization(request):
    return render(request, 'music/authorization.html', {'title': 'Вхід', 'menu_selected': 'authorization'})
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


menu = [{'title':'Завдання', 'url_name':'task'}]


def index(request):
    posts = Song.objects.all()
    return render(request, 'music/index.html', {'posts': posts, 'menu': menu, 'title': 'Головна сторрінка'})


def task(request):
    return render(request, 'music/task.html', {'menu': menu, 'title': 'Завдання', 'menu_selected':'task'})


def genres(request):
    infogenre = Genre.objects.all()
    return render(request, 'music/genres.html', {'infogenre': infogenre, 'menu': menu, 'title': 'Жанри'})


def songs(request):
    infosong = Song.objects.all()
    return render(request, 'music/songs.html', {'infosong': infosong, 'menu': menu, 'title': 'Пісні', 'menu_selected':'songs'})


def authors(request):
    infoauthor = Author.objects.all()
    return render(request, 'music/authors.html', {'infoauthor': infoauthor, 'menu': menu, 'title': 'Автори', 'menu_selected':'authors'})


def authorslist(request):
    infoauthorlist = AuthorList.objects.all()
    return render(request, 'music/authorslist.html', {'infoauthorlist': infoauthorlist, 'menu': menu, 'title': 'Перелік авторів'})


def libraries(request):
    infolibrary = Library.objects.all()
    return render(request, 'music/libraries.html', {'infolibrary': infolibrary, 'menu': menu, 'title': 'Бібліотеки', 'menu_selected':'libraries'})


def librarieslist(request):
    infolibrarylist = LibraryList.objects.all()
    return render(request, 'music/librarieslist.html', {'infolibrarylist': infolibrarylist, 'menu': menu, 'title': 'Перелік бібліотек'})


def singers(request):
    infosinger = Singer.objects.all()
    return render(request, 'music/singers.html', {'infosinger': infosinger, 'menu': menu, 'title': 'Співаки', 'menu_selected':'singers'})


def singerslist(request):
    infosingerlist = SingerList.objects.all()
    return render(request, 'music/singerslist.html', {'infosingerlist': infosingerlist, 'menu': menu, 'title': 'Перелік співаків'})


def users(request):
    infouser = User.objects.all()
    return render(request, 'music/users.html', {'infouser': infouser, 'menu': menu, 'title': 'Користувачі'})


def usersrating(request):
    inforating = Rating.objects.all()
    return render(request, 'music/usersrating.html', {'inforating': inforating, 'menu': menu, 'title': 'Рейтинг пісень'})
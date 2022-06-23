from django.http import HttpResponse
from django.shortcuts import render
from .models import *


menu = ["Завдання", "Додати"]


def index(request):
    posts = Song.objects.all()
    return render(request, 'music/index.html', {'posts': posts, 'menu': menu, 'title': 'Головна сторрінка'})


def task(request):
    return render(request, 'music/task.html', {'title': 'Завдання'})


def songs(request):
    return HttpResponse("<h1>Songs</h1>")
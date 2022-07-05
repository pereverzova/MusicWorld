from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('task/', task, name='task'),
    path('genre/<int:genre_id>/', genre, name='genre'),
    path('song/<int:song_id>/', song, name='song'),
    path('author/<int:author_id>/', author, name='author'),
    path('singer/<int:singer_id>/', singer, name='singer'),
    path('library/<int:library_id>/', library, name='library'),
    path('authors/', authors, name='authors'),
    path('singers/', singers, name='singers'),
    path('libraries/', libraries, name='libraries'),
    path('add/', add, name='add'),
]
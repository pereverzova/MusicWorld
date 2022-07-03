from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('task/', task, name='task'),

    path('genre1/', genre1, name='genre1'),
    path('genre2/', genre2, name='genre2'),

    path('songs/', songs, name='songs'),
    path('authors/', authors, name='authors'),
    path('authorslist/', authorslist, name='authorslist'),
    path('libraries/', libraries, name='libraries'),
    path('librarieslist/', librarieslist, name='librarieslist'),
    path('singers/', singers, name='singers'),
    path('singerslist/', singerslist, name='singerslist'),
    path('users/', users, name='users'),
    path('usersrating/', usersrating, name='usersrating'),
]
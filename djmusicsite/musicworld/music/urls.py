from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('task/', task, name='task'),
    path('genres/', genres),
    path('songs/', songs),
    path('authors/', authors),
    path('authorslist/', authorslist),
    path('libraries/', libraries),
    path('librarieslist/', librarieslist),
    path('singers/', singers),
    path('singerslist/', singerslist),
    path('users/', users),
    path('usersrating/', usersrating),
]
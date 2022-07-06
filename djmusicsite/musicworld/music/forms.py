import genres as genres
from django import forms
from .models import *


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_name', 'album', 'language', 'release_date', 'time', 'genre', 'photo']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_firstname', 'author_lastname', 'bio', 'photo']


class AuthorListForm(forms.ModelForm):
    class Meta:
        model = AuthorList
        fields = ['author', 'song']


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = ['singer_firstname', 'singer_lastname', 'group', 'pseudonym', 'bio', 'photo']


class SingerListForm(forms.ModelForm):
    class Meta:
        model = SingerList
        fields = ['singer', 'song']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_nickname']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'song', 'user_grade']


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['library_name']


class LibraryListForm(forms.ModelForm):
    class Meta:
        model = LibraryList
        fields = ['library', 'song']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']
from django import forms
from .models import *

class Song(forms.Form):
    song_name = forms.CharField(max_length=64, label="Пісні")
    album = forms.CharField(max_length=64, label="Альбом")
    language = forms.CharField(max_length=64, label="Мова")
    #release_date = forms.DateField(null=True, blank=True, label="")
    time = forms.CharField(max_length=64, label="Тривалість")
    #genre = forms.ForeignKey(Genre, on_delete=models.CASCADE, label="Жанр")
    #photo = forms.ImageField(upload_to="photos/%Y/%m/%d/", label="Фото")
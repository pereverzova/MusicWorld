from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=64)


class Author(models.Model):
    author_firstname = models.CharField(max_length=64)
    author_lastname = models.CharField(max_length=64)
    bio = models.TextField(blank=True)


class Song(models.Model):
    song_name = models.CharField(max_length=64)
    album = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    creating_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Library(models.Model):
    library_name = models.CharField(max_length=64)


class LibraryList(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)


class Singer(models.Model):
    singer_firstname = models.CharField(max_length=64)
    singer_lastname = models.CharField(max_length=64)
    group = models.CharField(max_length=64)
    pseudonym = models.CharField(max_length=64)
    bio = models.TextField(blank=True)


class SingerList(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Author(models.Model):
    author_firstname = models.CharField(max_length=64)
    author_lastname = models.CharField(max_length=64)
    bio = models.TextField(blank=True)


class AuthorList(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class User(models.Model):
    user_nickname = models.CharField(max_length=64)


class Raiting(models.Model):
    user_grade = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

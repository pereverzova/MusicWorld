from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=64)

    def __str__(self):
        return self.genre_name


class Song(models.Model):
    song_name = models.CharField(max_length=64)
    album = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=64)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name


class Library(models.Model):
    library_name = models.CharField(max_length=64)

    def __str__(self):
        return self.library_name


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

    def __str__(self):
        return self.author_lastname


class AuthorList(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class User(models.Model):
    user_nickname = models.CharField(max_length=64)

    def __str__(self):
        return self.user_nickname


class Rating(models.Model):
    user_grade = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

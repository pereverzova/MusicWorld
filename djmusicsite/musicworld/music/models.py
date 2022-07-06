from django.db import models
from django.urls import reverse


class Genre(models.Model):
    genre_name = models.CharField(max_length=64, verbose_name="Жанр")

    def __str__(self):
        return self.genre_name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name = 'Жанри'
        verbose_name_plural = 'Жанри'


class Song(models.Model):
    song_name = models.CharField(max_length=64, verbose_name="Пісня")
    album = models.CharField(max_length=64, verbose_name="Альбом")
    language = models.CharField(max_length=64, verbose_name="Мова")
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата випуску")
    time = models.CharField(max_length=64, verbose_name="Тривалість")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse('song', kwargs={'song_id': self.pk})

    class Meta:
        verbose_name = 'Пісні'
        verbose_name_plural = 'Пісні'


class Library(models.Model):
    library_name = models.CharField(max_length=64, verbose_name="Бібліотека")

    def __str__(self):
        return self.library_name

    def get_absolute_url(self):
        return reverse('library', kwargs={'library_id': self.pk})

    class Meta:
        verbose_name = 'Бібліотеки'
        verbose_name_plural = 'Бібліотеки'


class LibraryList(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Пісня")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name="Бібліотека")

    class Meta:
        verbose_name = 'Перелік бібліотек'
        verbose_name_plural = 'Перелік бібліотекеки'


class Singer(models.Model):
    singer_firstname = models.CharField(max_length=64, verbose_name="Ім'я")
    singer_lastname = models.CharField(max_length=64, verbose_name="Прізвище")
    group = models.CharField(max_length=64, verbose_name="Група")
    pseudonym = models.CharField(max_length=64, verbose_name="Псевдонім")
    bio = models.TextField(blank=True, verbose_name="Біографія")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    class Meta:
        verbose_name = 'Співаки'
        verbose_name_plural = 'Співаки'

    def get_absolute_url(self):
        return reverse('singer', kwargs={'singer_id': self.pk})


class SingerList(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, verbose_name="Співак")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Пісня")

    class Meta:
        verbose_name = 'Перелік співаків'
        verbose_name_plural = 'Перелік співаків'


class Author(models.Model):
    author_firstname = models.CharField(max_length=64, verbose_name="Ім'я")
    author_lastname = models.CharField(max_length=64, verbose_name="Прізвище")
    bio = models.TextField(blank=True, verbose_name="Біографія")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.author_lastname

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    class Meta:
        verbose_name = 'Автори'
        verbose_name_plural = 'Автори'


class AuthorList(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Пісня")

    class Meta:
        verbose_name = 'Перелік авторів'
        verbose_name_plural = 'Перелік авторів'


class User(models.Model):
    user_nickname = models.CharField(max_length=64, verbose_name="Користувач")

    def __str__(self):
        return self.user_nickname

    class Meta:
        verbose_name = 'Користувачі'
        verbose_name_plural = 'Користувачі'


class Rating(models.Model):
    user_grade = models.IntegerField(verbose_name="Оцінка(від 1 до 5)")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Пісня")

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'

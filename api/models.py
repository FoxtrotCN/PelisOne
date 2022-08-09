from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=155)


class Cast(models.Model):
    name = models.CharField(max_length=155)


# class Tag(models.Model):
#     name = models.CharField(max_length=155)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=1000)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    cast = models.ForeignKey(Cast, on_delete=models.DO_NOTHING)

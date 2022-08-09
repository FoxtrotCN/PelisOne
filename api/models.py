from django.db import models


class Movie(models.Model):
    RELIGIOUS = 'RG'
    ACTION = 'AC'
    DRAMA = 'DR'
    COMEDY = 'CM'
    SCIENCE_FICTION = 'SF'
    THRILLER = 'THR'

    GENRE_CHOICES = [
        (RELIGIOUS, 'Religioso'),
        (ACTION, 'Accion'),
        (DRAMA, 'Drama'),
        (COMEDY, 'Comedia'),
        (SCIENCE_FICTION, 'Ciencia Ficcion'),
        (THRILLER, 'Triler')
    ]

    title = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=1000)
    genre = models.CharField(max_length=155, choices=GENRE_CHOICES, default='')


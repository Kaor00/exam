from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class FilmList(models.Model):
    name = models.TextField()
    description = models.TextField()
    date = models.TextField()


class Actors(models.Model):
    name = models.TextField()
    date = models.TextField()
    film = models.ManyToManyField(FilmList)

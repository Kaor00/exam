from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FilmList, Actors

admin.site.register(FilmList)

admin.site.register(Actors)

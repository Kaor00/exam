from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import FilmList, Actors


def index(request):
    lst = FilmList.objects.all()
    context = {
        'films': lst,
    }
    return render(request, 'films/index.html', context)


def film(request, id):
    f = FilmList.objects.all().filter(pk=id)
    for film in f:
        film.actors_list = film.actors_set.all()
    context = {
        'films': f
    }

    return render(request, 'films/film.html', context)

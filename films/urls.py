from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film/<int:id>/', views.film, name='film')
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("anagram/<str:letters>", views.anagram, name="anagram"),
    path("wordfit/<str:letters>", views.wordfit, name="wordfit"),
]

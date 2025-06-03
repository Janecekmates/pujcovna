
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pujcky/", views.seznam_pujcek, name="seznam_pujcek"),
]
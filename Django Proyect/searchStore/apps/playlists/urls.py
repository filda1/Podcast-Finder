from django.contrib import admin
from django.urls import path
from .views import Playlists

urlpatterns = [
    path('', Playlists, name="playlists"),
  
]
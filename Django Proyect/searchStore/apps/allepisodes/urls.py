from django.contrib import admin
from django.urls import path
from .views import Allepisodes

urlpatterns = [
    path('', Allepisodes, name="allepisodes"),
  
]
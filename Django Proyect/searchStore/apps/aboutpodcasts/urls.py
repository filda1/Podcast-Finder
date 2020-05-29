from django.contrib import admin
from django.urls import path
from .views import Aboutpodcasts

urlpatterns = [
    path('', Aboutpodcasts, name="aboutpodcasts"),
  
]
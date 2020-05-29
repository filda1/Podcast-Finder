from django.contrib import admin
from django.urls import path
from .views import Realtime

urlpatterns = [
    path('', Realtime, name="realtime"),
  
]
from django.contrib import admin
from django.urls import path
from .views import Home

urlpatterns = [
    path('', Home, name="home"),
  
]
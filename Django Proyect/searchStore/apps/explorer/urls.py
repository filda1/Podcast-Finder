from django.contrib import admin
from django.urls import path
from .views import Explorer

urlpatterns = [
    path('', Explorer, name="explorer"),
  
]
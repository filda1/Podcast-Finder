from django.contrib import admin
from django.urls import path
from .views import Readmoreacademy

urlpatterns = [
    path('', Readmoreacademy, name="readmoreacademy"),
  
]
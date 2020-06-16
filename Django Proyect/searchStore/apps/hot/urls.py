from django.contrib import admin
from django.urls import path
from .views import Hot

urlpatterns = [
    path('', Hot, name="hot"),
  
]
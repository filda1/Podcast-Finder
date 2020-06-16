from django.contrib import admin
from django.urls import path
from .views import Curated

urlpatterns = [
    path('', Curated, name="curated"),
  
]
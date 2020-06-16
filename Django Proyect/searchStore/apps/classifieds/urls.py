from django.contrib import admin
from django.urls import path
from .views import Classifieds

urlpatterns = [
    path('', Classifieds, name="classifieds"),
  
]
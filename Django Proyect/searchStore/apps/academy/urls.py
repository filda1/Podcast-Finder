from django.contrib import admin
from django.urls import path
from .views import Academy

urlpatterns = [
    path('', Academy, name="academy"),
  
]
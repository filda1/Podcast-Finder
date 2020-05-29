from django.contrib import admin
from django.urls import path
from .views import Best

urlpatterns = [
    path('', Best, name="best"),
  
]
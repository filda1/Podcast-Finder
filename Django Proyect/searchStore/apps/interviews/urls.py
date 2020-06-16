from django.contrib import admin
from django.urls import path
from .views import Interviews

urlpatterns = [
    path('', Interviews, name="interviews"),
  
]
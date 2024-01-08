from django.contrib import admin
from django.urls import path, include
from .views import robots_txt, floder

urlpatterns = [
    path("", robots_txt),
    path("", floder),
]
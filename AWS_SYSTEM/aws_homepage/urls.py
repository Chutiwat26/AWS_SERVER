from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
]
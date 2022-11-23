from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('admin-page/', AdminPage, name='admin-page'),
]
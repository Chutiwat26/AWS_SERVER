from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('purchase-add-customer/', AddCustomer, name='purchase-add-customer'),
]
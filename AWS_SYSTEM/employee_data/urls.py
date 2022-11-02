from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('intranet-home/', EmployeeHome, name='aws-system-home'),
    path('login/', EmployeeLogin, name='login-page'),
    path('logout/', EmployeeLogout, name='logout-page'),
    path('register/', EmployeeRegister, name='register-page'),
    
]
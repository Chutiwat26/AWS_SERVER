from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('workshop-home/', WorkshopHome, name='aws-system-home'),
    path('workshop-detail/<int:drawing_id>', ShowDrawingDetail, name='workshop-detail-page'),
]
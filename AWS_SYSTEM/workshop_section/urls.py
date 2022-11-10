from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('workshop-home/', WorkshopHome, name='workshop-home-page'),
    path('qc-home/', QualityControlHome, name='qc-home-page'),
    path('workshop-detail/<int:drawing_id>', ShowDrawingDetail, name='workshop-detail-page'),
]
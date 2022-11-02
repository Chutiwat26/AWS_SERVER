from unicodedata import name
from django.urls import path
from .views import *


urlpatterns = [
    path('drawing-upload/', DraftsMan, name='drawing-upload'),
    path('drawing-upload-done/', DrawingUploadDone, name='drawing-upload-done'),
    path('drawing-status/', DrawingStatus, name='drawing-status'),
    path('drawing-detail/<int:drawing_id>', ShowDrawingDetail, name='drawing-detail-page'),
]
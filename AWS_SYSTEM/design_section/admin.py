from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(JobTiltle)
admin.site.register(UserJob)
admin.site.register(PictureDetail)
admin.site.register(DrawingDetail)
admin.site.register(JobFile)
admin.site.register(FileDetail)
admin.site.register(PictureFile)
admin.site.register(DrawingFile)
admin.site.register(DrawingAssignment)
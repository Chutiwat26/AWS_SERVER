from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PurchaseOrderTitle)
admin.site.register(UserPurchaseOrder)
admin.site.register(QuotationFile)
admin.site.register(PoDocumentFile)
admin.site.register(QuotationDetail)
admin.site.register(PoDocumentDetail)
admin.site.register(PurchaseOrderFile)
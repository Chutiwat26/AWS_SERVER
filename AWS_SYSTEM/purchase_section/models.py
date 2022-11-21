from django.db import models
from django.contrib.auth.models import User
from design_section.models import FileDetail, PictureFile
from customer_section.models import Customers

# Create your models here.
class PurchaseOrderTitle(models.Model):
    title = models.CharField(max_length=200) #next time will link with PO
    customer = models.ForeignKey(Customers, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    receive_datetime = models.DateTimeField(null=True, blank=True)
    finish_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class UserPurchaseOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    purchase_order_id = models.ForeignKey(PurchaseOrderTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.purchase_order_id.title

class QuotationFile(models.Model):
    path = models.FileField(upload_to='file', null=True, blank=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

    def __str__(self):
        text = str(self.pk) + '.' + str(self.name)
        return text

class PoDocumentFile(models.Model):
    path = models.FileField(upload_to='file', null=True, blank=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

    def __str__(self):
        text = str(self.pk) + '.' + str(self.name)
        return text

class QuotationDetail(models.Model):
    quotation_id = models.ForeignKey(QuotationFile, on_delete=models.CASCADE)
    detail_id = models.ForeignKey(FileDetail, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.quotation_id.pk) + '.' + str(self.quotation_id.name)
        return text

class PoDocumentDetail(models.Model):
    po_document_id = models.ForeignKey(PoDocumentFile, on_delete=models.CASCADE)
    detail_id = models.ForeignKey(FileDetail, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.po_document_id.pk) + '.' + str(self.po_document_id.name)
        return text

class PurchaseOrderFile(models.Model):
    purchase_order_id = models.ForeignKey(PurchaseOrderTitle, on_delete=models.CASCADE)
    picture_id = models.ForeignKey(PictureFile, on_delete=models.CASCADE)
    quotation_id = models.ForeignKey(QuotationFile, on_delete=models.CASCADE)
    po_document_id = models.ForeignKey(PoDocumentFile, on_delete=models.CASCADE)

    def __str__(self):
        return self.purchase_order_id.title
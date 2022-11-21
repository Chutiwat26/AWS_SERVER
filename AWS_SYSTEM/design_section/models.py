from email.policy import default
from multiprocessing import JoinableQueue
from django.db import models
from django.contrib.auth.models import User
from customer_section.models import Customers
from employee_data.models import EmployeeProfile


# Create your models here.


class JobTiltle(models.Model):
    title = models.CharField(max_length=200) #next time will link with PO
    description = models.TextField(null=True, blank=True)
    submit_date = models.DateTimeField(null=True, blank=True)
    process_date = models.DateTimeField(null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(Customers, on_delete=models.DO_NOTHING)

    def __str__(self):
        text = str(self.pk) + '.' + str(self.title)
        return text

class UserJob(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    job_id = models.ForeignKey(JobTiltle, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user_id)

class FileDetail(models.Model):
    detail = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=40)   #waiting,processing, QC, repair, reject, finished, canceled
    submit_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name



class PictureFile(models.Model):
    path = models.ImageField(upload_to='picture', null=True, blank=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

    def __str__(self):
        text = str(self.pk) + '.' + str(self.name)
        return text

class DrawingFile(models.Model):
    path = models.FileField(upload_to='file', null=True, blank=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20) #waiting,processing, QC, repair, reject, finished, canceled

    def __str__(self):
        text = str(self.pk) + '.' + str(self.name)
        return text

class PictureDetail(models.Model):
    picture_id = models.ForeignKey(PictureFile, on_delete=models.CASCADE)
    detail_id = models.ForeignKey(FileDetail, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.picture_id.pk) + '.' + str(self.picture_id.name)
        return text


class DrawingDetail(models.Model):
    drawing_id = models.ForeignKey(DrawingFile, on_delete=models.CASCADE)
    detail_id = models.ForeignKey(FileDetail, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.drawing_id.pk) + '.' + str(self.drawing_id.name)
        return text


class JobFile(models.Model):
    job_id = models.ForeignKey(JobTiltle, on_delete=models.DO_NOTHING)
    picture_id = models.ForeignKey(PictureFile, on_delete=models.DO_NOTHING , null=True, blank=True)
    drawing_id = models.ForeignKey(DrawingFile, on_delete=models.DO_NOTHING , null=True, blank=True)

    def __str__(self):
        text = str(self.job_id)
        return text

class DrawingAssignment(models.Model):
    drawing_id = models.ForeignKey(DrawingFile, on_delete=models.DO_NOTHING)
    sender_username = models.CharField(max_length=200)
    receiver_username = models.CharField(max_length=200, null=True, blank=True)
    job_state = models.CharField(max_length=200) #waiting,processing, QC, repair, reject, finished, canceled
    detail_id = models.ForeignKey(FileDetail, on_delete=models.DO_NOTHING , null=True, blank=True)

    def __str__(self):
        return self.drawing_id.name




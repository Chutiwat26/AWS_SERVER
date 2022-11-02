from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    nation_id = models.CharField(max_length=13, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        text = str(self.user.pk) + "." + self.user.username
        return text

class CompanyPosition(models.Model):
    position_name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        text = str(self.pk) + "." + self.position_name
        return text

class ProfilePosition(models.Model):
    profile_id = models.ForeignKey(EmployeeProfile, on_delete=models.DO_NOTHING)
    position_id = models.ForeignKey(CompanyPosition, on_delete=models.DO_NOTHING) 

    def __str__(self):
        text = str(self.profile_id)
        return text

    


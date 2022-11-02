from django.db import models

# Create your models here.
class Customers(models.Model):
    full_name = models.CharField(max_length=100)
    initial_name = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.initial_name
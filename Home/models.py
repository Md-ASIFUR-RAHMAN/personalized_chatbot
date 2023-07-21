from django.db import models

# Create your models here.

class Registration(models.Model):
    ID = models.AutoField(primary_key = True)
    Name = models.CharField(blank=True, max_length=500, null=True)
    Phone = models.CharField(blank=True, max_length=500, null=True,unique=True)
    Email = models.CharField(blank=True, max_length=500, null=True, unique=True)
    Gender = models.CharField(blank=True, max_length=500, null=True)
    Password = models.CharField(blank=True, max_length=500, null=True)
    pro_pic = models.CharField(blank=True, max_length=500, null=True)
    last_login = models.CharField(blank=True, max_length=500, null=True)
    OTP = models.CharField(blank=True, max_length=500, null=True)
    type = models.CharField(blank=True, max_length=1000, null=True)





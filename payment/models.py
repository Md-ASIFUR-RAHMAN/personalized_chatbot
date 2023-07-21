from django.db import models

# Create your models here.


class payment_info(models.Model):
    buyer_id  = models.CharField(blank=True, max_length=500, null=True)
    buyer_name  = models.CharField(blank=True, max_length=500, null=True)
    CardNumber  = models.CharField(blank=True, max_length=500, null=True)
    CardName  = models.CharField(blank=True, max_length=500, null=True)
    ExpiryDate = models.CharField(blank=True, max_length=20, null=True)
    amount = models.CharField(blank=True, max_length=500, null=True)
    buy_date = models.DateField(blank=True, max_length=50, null=True)
    Status = models.CharField(blank=True, max_length=50, null=True)


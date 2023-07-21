from django.db import models

# Create your models here.



class FAQ(models.Model):
    Idd = models.CharField(blank=True, max_length=500, null=True)
    qs1 = models.CharField(blank=True, max_length=500, null=True)
    qs2 = models.CharField(blank=True, max_length=500, null=True)
    qs3 = models.CharField(blank=True, max_length=500, null=True)
    qs4 = models.CharField(blank=True, max_length=500, null=True)
    qs5 = models.CharField(blank=True, max_length=500, null=True)



    ans1 = models.CharField(blank=True, max_length=500, null=True)
    ans2 = models.CharField(blank=True, max_length=500, null=True)
    ans3 = models.CharField(blank=True, max_length=500, null=True)
    ans4 = models.CharField(blank=True, max_length=500, null=True)
    ans5 = models.CharField(blank=True, max_length=500, null=True)





class ChatFaq(models.Model):
    Idd = models.CharField(blank=True, max_length=500, null=True)
    Question = models.CharField(blank=True, max_length=1000, null=True)
    Answer = models.CharField(blank=True, max_length=1000, null=True)
    Dictionary = models.CharField(blank=True, max_length=1000, null=True)


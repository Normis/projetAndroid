from django.db import models

# Create your models here.

class Hopital(models.Model):
    name = models.CharField(max_length=50, blank=True, default='',primary_key=True)
    lat = models.CharField(max_length=100, blank=True, default='')
    lng = models.CharField(max_length=100, blank=True, default='')

class Profile(models.Model):
    email = models.CharField(max_length=50, blank=True, default='',primary_key=True)
    surname = models.CharField(max_length=30, blank=True, default='')
    name = models.CharField(max_length=30, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True, default='')
    age = models.CharField(max_length=100, blank=True, default='')
    hopital = models.ForeignKey(Hopital)

class HopitalTimeWait(models.Model):
    hopital = models.ForeignKey(Hopital)
    profile = models.ForeignKey(Profile)
    date = models.CharField(max_length=50,blank = True,default='')
    waitTime = models.CharField(max_length=50,blank = True,default='')
    rageQuit = models.CharField(max_length=5,blank = True,default='')

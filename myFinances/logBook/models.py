from itertools import count
from django.db import models

# Create your models here.

class account(models.Model):
    name=models.CharField(max_length=50)

class subaccount(models.Model):
    name=models.CharField(max_length=50)
    ledgerAccount=models.CharField(max_length=50)

class accountingEvent(models.Model):
    fecha=models.DateTimeField()
    count=models.CharField(max_length=50)
    subcount=models.CharField(max_length=50)
    value=models.FloatField()
    detail=models.CharField(max_length=150)


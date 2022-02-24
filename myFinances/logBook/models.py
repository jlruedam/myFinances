from itertools import count
from django.db import models

# Create your models here.

class account(models.Model):
    name=models.CharField(max_length=50)

class subaccount(models.Model):
    name=models.CharField(max_length=50)
    ledgerAccount=models.CharField(max_length=50)

class accountingEvent(models.Model):
    dateEvent=models.DateTimeField()
    account=models.CharField(max_length=50)
    subaccount=models.CharField(max_length=50)
    valueEvent=models.FloatField()
    descriptionEvent=models.CharField(max_length=150)


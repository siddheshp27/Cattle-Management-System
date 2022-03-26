from django.db import models
from django.utils import timezone

# Create your models here.

class Userdata(models.Model):
     username= models.CharField(max_length=30)
     email= models.EmailField()
     password= models.CharField(max_length=30)
     conf_pass = models.CharField(max_length=30)

class Animaldata(models.Model):
     Eartag= models.IntegerField()
     DOB= models.DateField()
     sex= models.CharField(max_length=10)
     breed=models.CharField(max_length=30)
     stage= models.CharField(max_length=20)
     calvings= models.IntegerField(default=0)
     

class Dailydata(models.Model):
     date= models.DateField()
     eartag= models.IntegerField()
     totalmilk= models.IntegerField()
     production=models.CharField(max_length=30)
     calvings= models.IntegerField(default=0)
     

class Heatdata(models.Model):
     date= models.DateField()
     eartag= models.IntegerField()
     breed=models.CharField(max_length=30)


class Milk(models.Model):
     totalmilk= models.IntegerField()
     date= models.DateField()

class Account(models.Model):
     date= models.DateField()
     totalmilk= models.IntegerField()
     Earnings_bulls= models.IntegerField()
     Earnings_extra= models.IntegerField()
     Expenditure_Feeder= models.IntegerField()
     Expenditure_Medical= models.IntegerField()
     Expenditure_Labour= models.IntegerField()
     Expenditure_Eexpenses= models.IntegerField()

     

  
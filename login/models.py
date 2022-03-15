from django.db import models

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
     # heat=models.DateField()

class Dailydata(models.Model):
     date= models.DateField()
     eartag= models.IntegerField()
     totalmilk= models.IntegerField()
     production=models.CharField(max_length=30)

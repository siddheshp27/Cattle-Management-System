from django.contrib import admin
from .models import Userdata,Animaldata,Dailydata
# Register your models here.

@admin.register(Userdata)

class Userdetails(admin.ModelAdmin):
    list_display = ['username','email','password','conf_pass']

@admin.register(Animaldata)

class Animaldata(admin.ModelAdmin):
    list_display = ['Eartag','DOB','sex','breed','stage','calvings']

@admin.register(Dailydata)

class Dailydata(admin.ModelAdmin):
    list_display = ['eartag','date','totalmilk','production']
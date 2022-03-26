from django.contrib import admin
from .models import Userdata,Animaldata,Dailydata,Heatdata,Milk,Account
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

@admin.register(Heatdata)

class Heatdata(admin.ModelAdmin):
    list_display = ['eartag','date','breed']

@admin.register(Milk)

class Milk(admin.ModelAdmin):
    list_display = ['date','totalmilk']

@admin.register(Account)

class Account(admin.ModelAdmin):
    list_display = ['date','totalmilk','Earnings_bulls','Earnings_extra','Expenditure_Feeder','Expenditure_Medical','Expenditure_Labour','Expenditure_Eexpenses']
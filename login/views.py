from django.shortcuts import render, redirect
from .models import Userdata
from .models import Animaldata,Dailydata
from django.contrib import messages
from datetime import datetime

def register(request):
    if request.method == "POST":
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       conf_pass = request.POST['con_pass']
       if Userdata.objects.filter(username=username).exists():
           messages.error(request, 'This username is already taken')
           return redirect('Registration')
       elif Userdata.objects.filter(email=email).exists():
           messages.error(request, 'This email is already taken')
           return redirect('Registration')
       elif(password != conf_pass):
           messages.error(request, 'Please enter same password')
           return redirect('Registration')
       else:
           students = Userdata(username=username, email=email, password=password, conf_pass=conf_pass)
           students.save()
           messages.success(request, "Register Successfully")
           return redirect('/')
    return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        passw = request.POST['pass']
        if Userdata.objects.filter(email=email).exists():
            if Userdata.objects.filter(password=passw).exists():
                return redirect('home')
            else:
                messages.error(request, 'Incorrect password')
                return redirect('/')
        else:
            messages.error(request, 'Incorrect email')
            return redirect('/')
    return render(request, 'login.html')

def home(request):
   totemilk=0
   totallst=[]
   if request.method=="POST" :
       finddate=request.POST['FindDate']
       sort=Dailydata.objects.values('date')   
       s={items['date'] for items in sort}
       for i in s:
         tempstore =Dailydata.objects.filter(date=finddate)
       tagss=tempstore.values('eartag')
       settags={items['eartag'] for items in tagss}
       tags=list(settags)
       ec=0
       mic=0
       totmilk=0
       while ec < len(tags):
         tempdataet=tempstore.filter(eartag=tags[ec])
         tempmilkss=tempdataet.values('totalmilk')
         tempmilks=[items['totalmilk'] for items in tempmilkss]
         mic=0
         totemilk=0
         while(mic<len(tempmilks)):
          totemilk+=tempmilks[mic]
          mic+=1
         totallst.append(totemilk)
         totmilk+=totemilk
         ec+=1
       print(ec)    
       storeall=tags
       parmas={"storeall" : storeall,"totallst":totallst,"varint":0} 
       return render(request, 'fetch.html',parmas)  
       
   return render(request, 'home.html')

def reccomandation(request):
    return render(request, 'reccomantion.html')

def schemes(request):
    return render(request, 'govtschemes.html')

def about(request):
    return render(request, 'about.html')

def animal_registration(request):
   if request.method == "POST":
        Eartag = request.POST['full-name']
        DOB = request.POST['DOB']
        sex = request.POST['sex']
        breed = request.POST['boc']
        stage = request.POST['stage']
        calvings = request.POST['present_address']
        if Animaldata.objects.filter(Eartag=Eartag).exists():
            messages.error(request, 'This Eartag is already registered')
            
        else:
            animals = Animaldata(Eartag=Eartag, DOB=DOB, sex=sex, breed=breed, stage=stage, calvings=calvings)
            animals.save()
            messages.success(request, "register successfully")
   return render(request,'animal_registration.html')

def alldata(request):
    storeall=Animaldata.objects.all()
    parmas={'storeall': storeall}
    if request.method == "POST" :
        HEAT_str = request.POST['Missed Heat']
        count=request.POST['Submit']
        


        # Heat= datetime.strptime(HEAT_str,'%Y-%m-%d')
        # today=datetime.now()
        # print(type(Heat))
        # print(today-Heat)
    
    
    return render(request,'AllData.html',parmas) 

def milking(request):
    sort=Animaldata.objects.values('stage')   
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Milking")
        parmas={'storeall': storeall}
    return render(request,'milking.html' ,parmas)

def pregnant(request):
    sort=Animaldata.objects.values('stage')   
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Pregnant")
        parmas={'storeall': storeall}
    return render(request,'pregnant.html' ,parmas)

def calf(request):
    sort=Animaldata.objects.values('stage')   
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Calf")
        parmas={'storeall': storeall}
    return render(request,'calving.html' ,parmas)

def bulls(request):
    sort=Animaldata.objects.values('stage')   
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(sex="MALE")
        parmas={'storeall': storeall}
    return render(request,'bulls.html' ,parmas)

def female(request):
    sort=Animaldata.objects.values('sex') 
    print(sort)  
    s={items['sex'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(sex="FEMALE")
        parmas={'storeall': storeall}
    return render(request,'Heat.html' ,parmas)

def account(request):
    sort=Animaldata.objects.values('stage')   
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Milking")
        parmas={'storeall': storeall}
    return render(request, 'milking.html',parmas)

def morning(request):
    sort=Animaldata.objects.values('stage') 
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Milking")
    tags=storeall.values('Eartag')
    if request.method=="POST": 
     j=request.POST['submit']   
     z=int(j)
     tagtemp=tags[(z-1)]      
     tag=tagtemp["Eartag"]
     milk =request.POST['Morning'] 
     date =request.POST['Date'] 
     milk = Dailydata(eartag=tag,date=date,totalmilk=milk,production="Morning")
     milk.save()
     return redirect('/Morning') 
    
    parmas={'storeall': storeall}
    return render(request, 'morning.html',parmas)

def afternoon(request):
    sort=Animaldata.objects.values('stage') 
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Milking")
    tags=storeall.values('Eartag')
    if request.method=="POST": 
     j=request.POST['submit']   
     z=int(j)
     tagtemp=tags[(z-1)]      
     tag=tagtemp["Eartag"]
     milk =request.POST['Afternoon'] 
     date =request.POST['Date'] 
     milk = Dailydata(eartag=tag,date=date,totalmilk=milk,production="Afternoon")
     milk.save()
     return redirect('/Afternoon') 
    
    parmas={'storeall': storeall}

            
    return render(request, 'afternoon.html',parmas)

def evening(request):
    sort=Animaldata.objects.values('stage') 
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Milking")
    tags=storeall.values('Eartag')
    if request.method=="POST": 
     j=request.POST['submit']   
     z=int(j)
     tagtemp=tags[(z-1)]      
     tag=tagtemp["Eartag"]
     milk =request.POST['Evening'] 
     date =request.POST['Date'] 
     milk = Dailydata(eartag=tag,date=date,totalmilk=milk,production="Evening")
     milk.save()
     return redirect('/Evening') 
    
    parmas={'storeall': storeall}

            
    return render(request, 'evening.html',parmas)


def heat(request):
    sort=Animaldata.objects.values('stage') 
    s={items['stage'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(stage="Adult")
    tags=storeall.values('Eartag')
    if request.method=="POST": 
     j=request.POST['submit']   
     z=int(j)
     tagtemp=tags[(z-1)]      
     tag=tagtemp["Eartag"]
     date =request.POST['Date'] 
     print(date)
    #  milk = Dailydata(eartag=tag,date=date,totalmilk=milk,production="Morning")
    #  milk.save()
     return redirect('/HeatPeriod') 
    
    parmas={'storeall': storeall}
    return render(request, 'Heat.html',parmas)


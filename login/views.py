from django.shortcuts import render, redirect
from .models import Userdata
from .models import Animaldata,Dailydata,Heatdata,Milk,Account
from django.contrib import messages
from datetime import datetime,timedelta


def register(request):
    if request.method == "POST":
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       conf_pass = request.POST['con_pass']
       if Userdata.objects.filter(username=username).exists():
           messages.error(request, 'This username is already taken')
           return redirect('/Registration')
       elif Userdata.objects.filter(email=email).exists():
           messages.error(request, 'This email is already taken')
           return redirect('/Registration')
       elif(password != conf_pass):
           messages.error(request, 'Please enter same password')
           return redirect('/Registration')
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
       storeall=tags
       acc=Milk(date=finddate,totalmilk=totmilk)
       acc.save()
       parmas={"storeall" : storeall,"totallst":totallst} 
       return render(request, 'fetch.html',parmas)  
       
   return render(request, 'home.html')

def reccomandation(request):
    return render(request, 'recommendation.html')

def schemes(request):
    return render(request, 'govtscheme.html')

def about(request):
    return render(request, 'about.html')

def animal_registration(request):
   if request.method == "POST":
        Eartag = request.POST['full-name']
        DOB = request.POST['DOB']
        sex = request.POST['sex']
        breed = request.POST['boc']
        stage = request.POST['stage']
        calving = request.POST['present_address']
        if calving == '' :
         calving = 0 
        if Animaldata.objects.filter(Eartag=Eartag).exists():
            messages.error(request, 'This Eartag is already registered')
            
        else:
            animals = Animaldata(Eartag=Eartag, DOB=DOB, sex=sex, breed=breed, stage=stage, calvings=calving)
            animals.save()
            messages.success(request, "register successfully")
   return render(request,'animal_registration.html')

def alldata(request):
    storeall=Animaldata.objects.all()
    parmas={'storeall': storeall}
    if request.method == "POST" :
        HEAT_str = request.POST['Missed Heat']
        count=request.POST['Submit']    
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
    s={items['sex'] for items in sort}
    for i in s:
        storeall =Animaldata.objects.filter(sex="FEMALE")
        parmas={'storeall': storeall}
    return render(request,'Heat.html' ,parmas)

def account(request):
    store=Milk.objects.values('totalmilk')
    Today=store.filter(date=datetime.now())
    Tmilk={items['totalmilk'] for items in Today}
    storeall=max(Tmilk)

    parmas={"storeall":storeall}
    if request.method=="POST" :
        Earnings_bulls=request.POST['Ebull']
        Earnings_extra=request.POST['Eearn']
        Expenditure_Feeder=request.POST['Feeder']
        Expenditure_Medical=request.POST['Medical']
        Expenditure_Labour=request.POST['Labour']
        Expenditure_Eexpenses=request.POST['Eexpenses']   
        acc=Account(Earnings_bulls=Earnings_bulls,Earnings_extra=Earnings_extra,Expenditure_Feeder=Expenditure_Feeder,Expenditure_Medical=Expenditure_Medical,Expenditure_Labour=Expenditure_Labour,Expenditure_Eexpenses=Expenditure_Eexpenses,date=datetime.now(),totalmilk=storeall)
        acc.save()
    return render(request, 'account.html',parmas)

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
    breed_=storeall.values('breed')
    if request.method=="POST": 
     j=request.POST['submit'] 
     print(j)  
     z=int(j)
     tagtemp=tags[(z-1)]      
     breedtemp=breed_[(z-1)]      
     tag=tagtemp["Eartag"]
     breed_=breedtemp["breed"]
     date =request.POST['Date'] 
     heat_ = Heatdata(eartag=tag,date=date,breed=breed_)
     heat_.save()
     return redirect('/HeatPeriod')
    parmas={'storeall': storeall}
    return render(request, 'Heat.html',parmas)
 


def heatcalc(request) :
    s=[]
    Heat=[]
    Diff=[]
    date1=[]
    Tdate1=[]
    date2=[]
    Tdate2=[]
    storeall={"storeall" :  [] }
    TEartag=Heatdata.objects.values('eartag')
    Tbreed=Heatdata.objects.values('breed')
    store=Heatdata.objects.values('date')
    data=[items['date'] for items in store]
    for i in data:
        Tapp1= i + timedelta(days=18)
        app1=str(Tapp1)
        Tdate1.append(app1)
    
    for i in data:
        Tapp2= i + timedelta(days=24)
        app2=str(Tapp2) 
        Tdate2.append(app2)
    
    Eartag=[items['eartag'] for items in TEartag]
    breed=[items['breed'] for items in Tbreed]
    
    parmas={"Eartag":[],"breed":[],"date1":[],"date2":[]}
    today=datetime.now()

    for i in data:
     s.append(str(i))
    
    for i in s:
        Heat.append(datetime.strptime(i,'%Y-%m-%d'))

    for i in Heat:
        res=today-i
        resf=res.total_seconds()/86400
        Diff.append(resf)

    Tstoredict={"Eartag":Eartag,"breed":breed,"datediff":Diff,"date":data}
    countstore=0
    temp=Tstoredict['Eartag'][0]

    for i in Tstoredict['datediff']:

        if i<25 and i>17 :
         class parmas :
          Eartag=(Tstoredict['Eartag'][countstore])
          breed = Tstoredict['breed'][countstore]
          date1 = Tdate1[countstore]
          date2 = Tdate2[countstore]
         storeall["storeall"].append(parmas)
        
        countstore +=1
    return render(request, 'HeatDisplay.html',storeall)
 
def fetchacc(request) :
    if request.method == "POST" :
     fetch_date=request.POST['FindDate']
     store=Account.objects.all()
     date_data=store.filter(date=fetch_date)
     totmi=date_data.values('totalmilk')
     earnmi=totmi[0]['totalmilk'] * 37.5
     print(earnmi)
     Earn_bull=Account.objects.values('Earnings_bulls').filter(date=fetch_date)
     Earn_extra=Account.objects.values('Earnings_extra').filter(date=fetch_date)
     Feeder=Account.objects.values('Expenditure_Feeder').filter(date=fetch_date)
     Medical=Account.objects.values('Expenditure_Medical').filter(date=fetch_date)
     Labour=Account.objects.values('Expenditure_Labour').filter(date=fetch_date)
     Eexpenses=Account.objects.values('Expenditure_Eexpenses').filter(date=fetch_date)
     totex=Feeder[0]['Expenditure_Feeder']+Medical[0]['Expenditure_Medical']+Labour[0]['Expenditure_Labour']+Eexpenses[0]['Expenditure_Eexpenses']
     totea=Earn_bull[0]['Earnings_bulls'] + Earn_extra[0]['Earnings_extra'] 
     totearn={'earn':totea}
     earnmilk={'total':earnmi}
     totexpenses={'expenses':totex}
     pro=earnmi + totea - totex
     profit={'inc':pro}
     params={'storeall':date_data,"totearn":totearn,"milkearn":earnmilk,"totexpenses":totexpenses,"profit":profit}
     print(params)
     return render(request,'fetchacc.html',params )
    return render(request,'dateacc.html')    


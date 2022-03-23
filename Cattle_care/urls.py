"""Cattle_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="lg"),
    path('Home', views.home, name="home"),
    path('Registration', views.register, name="Reg"),
    path('Reccomandation', views.reccomandation, name="Recc"),
    path('GovtSchemes', views.schemes, name="Schemes"),
    path('About', views.about, name="About"),
    path('AnimalRegistration', views.animal_registration, name="AniReg"),
    path('AllData', views.alldata, name="AllData"),
    path('Milking', views.milking, name="Milking"),
    path('Pregnant', views.pregnant, name="Pregnant"),
    path('Calf', views.calf, name="Calf"),
    path('Bulls', views.bulls, name="Bulls"),
    path('Female', views.female, name="Female"),
    path('Accounts', views.account, name="Accounts"),
    path('Morning', views.morning, name="Morning"),
    path('Afternoon', views.afternoon, name="Afternoon"),
    path('Evening', views.evening, name="Evening"),
    path('HeatPeriod', views.heat, name="HeatPeriod"),
]

"""iblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', home),
    path('donate/', donate),
    path('contact/', contact),
    path('about/', about),
    path('financials/', financials),
    path('ourteam/', ourteam),
    path('blogs/', blogs),
    path('video/', video),
    path('stories/', stories),
    path('solvecrisis/', solvecrisis),
    path('promise/', promise),
    path('donation/', donation),
    path('monthly/', monthly),
    path('community/', community),
    path('sponsorship/', sponsorship),
    path('watercrisis/', watercrisis),
    path('covid/', covid),
    path('waterhealth/', waterhealth),
    path('watereducation/', watereducation),
    path('hunger/', hunger),
    path('poverty/', poverty),
    path('scarcity/', scarcity),
    path('statistics/', statistics),
    path('images/', images),
    path('payment/', payment),
    path('process_payment/', process_payment),
    path('leader/', leader),
    path('employment/', employment),
    path('reviews/', reviews),
    path('teaching/', teaching),
    path('research/', research),
    path('fund/', fund),
    
    





    path('blog/<slug:url>', post),
    path('category/<slug:url>', category)
]

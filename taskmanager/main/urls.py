
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name ='index'),
    path('about.html', views.about, name='about_html'),
    path('shedule.html', views.shedule, name='shedule'),
]

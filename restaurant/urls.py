from django.contrib import admin 
from django.urls import path 
from .views import *
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path("menu/", MenuView.as_view()),
    path("booking/", BookingView.as_view())
]
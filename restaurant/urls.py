from django.contrib import admin 
from django.urls import path 
from .views import *
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [ 
    path('', views.index, name='index'),
    path("menu/", MenuView.as_view()),
    path("booking/", BookingView.as_view()),
    path("booking/<int:pk>", SingleBookingItemView.as_view()),
    path ('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuView.as_view()),
]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signIn/', views.signIn, name='signIn'),
    path('home/', views.home, name='home'),
    path('signUp/', views.signUp, name='signUp'),
    path("logout/", views.log_out, name="logout"),
]

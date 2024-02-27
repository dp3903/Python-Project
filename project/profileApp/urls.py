from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='signIn'),
    path('home/', views.home, name='home'),
    path('sign_up/', views.sign_up, name='signUp'),
    path("logout/", views.logout_request, name="logout"),
]

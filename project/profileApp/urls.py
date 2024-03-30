from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signIn/', views.signIn, name='signIn'),
    path('home/', views.home, name='home'),
    path('signUp/', views.signUp, name='signUp'),
    path("logout/", views.log_out, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("upload/", views.upload, name="upload"),
    path("template/", views.template, name="template"),
    path('editProfile/', views.UpdateUserView, name='editProfile'),
    path('deleteProfile/', views.DeleteUserProfile, name='deleteProfile'),
<<<<<<< HEAD
    path('search/',views.searchTemplate,name='searchTemplate'),
=======
    path('download/', views.download, name='download'),
    path('delete/', views.delete, name='delete'),
>>>>>>> b0cc2903fb99021a84c7549ce13459a6ed3e2695
]

from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, LoginForm, EditUserProfileForm
from .models import Users
from templateData.models import Template
import os
from django.views import generic
from django.urls import reverse_lazy
import sqlite3
from pathlib import Path

def signUp(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            profile_img = form.cleaned_data['profile_img']
            if password1 == password2:
                user = form.save()
                login(request, user)
                return redirect('home')  # Redirect to the home page or another page after successful registration
            else:
                form = CustomUserCreationForm()
                return render(request, 'signUp.html', {'username': username, 'email': email, 'status': 'Confirm password does not match the password.'})
        else:
            return render(request, 'signUp.html', {'status': 'Invalid data, Please try again.'})  # Pass form to template if form is invalid
    else:
        form = CustomUserCreationForm()
    return render(request, 'signUp.html')  # Pass form to template for initial rendering


def signIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or another page after successful login

        # Handle invalid login
        return render(request, 'signIn.html', {'status': False})
    else:
        return render(request, 'signIn.html', {'status': True})


# home page
def home(request):
    if request.user.is_authenticated:
        profileImg = Users.objects.filter(username = request.user.username).values_list('profile_img')
        templates = Template.objects.all()
        # templates = list(templates)
        # print(templates)
        # print(profileImg[0][0])
        # print(type(profileImg[0][0]))
        # print(profileImg[0][0] == '')
        context = {}
        if(profileImg[0][0] == ''):
            context = {
                'profile' : 'profile.jpg',
                'templates' : templates
            }
        else:
            context = {
                'profile' : profileImg[0][0][7:],
                'templates' : templates
            }
        print(context)

        return render(request, 'home.html', context)
    else:
        return redirect('signIn')

def log_out(request):
    logout(request)
    return redirect('signIn')


def profile(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            profileImg = Users.objects.filter(username = request.user.username).values_list('profile_img')
            # print(profileImg[0][0])
            # print(type(profileImg[0][0]))
            # print(profileImg[0][0] == '')
            context = {}
            if(profileImg[0][0] == ''):
                context = {
                    'profile' : 'profile.jpg'
                }
            else:
                context = {
                    'profile' : profileImg[0][0][7:]
                }
            print(context)
            return render(request, 'profile.html', context)
        else:
            return redirect('signIn')
    else:
        return redirect('signIn')

def upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            print('uploading template')
            print(request.POST)
            print(request.FILES)
            
            imgpath = 'static/templates/tempImages/'
            filepath = 'static/templates/tempFiles/'
            name = str(request.user.id) + '_' + request.POST['templateName']
            try:
                f = open(imgpath + name +'.jpg','x')
                f.close()
                f = open(filepath + name +'.zip','x')
                f.close()
                with open(imgpath + name +'.jpg', "wb+") as destination:
                    for chunk in request.FILES['templateImg'].chunks():
                        destination.write(chunk)
                with open(filepath + name +'.zip', "wb+") as destination:
                    for chunk in request.FILES['templateZip'].chunks():
                        destination.write(chunk)
                temp = Template()
                temp.templateId = str(request.user.id) + '_' + request.POST['templateName']
                temp.templateName = request.POST['templateName']
                temp.UID = request.user
                temp.description = request.POST['description']
                temp.date = request.POST['date']
                temp.totaldownloads = 0
                temp.templateZip = filepath + name
                temp.save()
            except FileExistsError :
                return HttpResponse('<h1>Template name already exists. Please try again with a different name.<h1>')
            except:
                if os.path.isfile(imgpath + name +'.jpg'):
                    os.remove(imgpath + name +'.jpg')
                if os.path.isfile(filepath + name +'.zip'):
                    os.remove(filepath + name +'.zip')
                return HttpResponse('<h1>Some error has occured. Please try again.</h1>')            
            print(temp)
            return HttpResponse('<h1>Successfully uploaded template...</h1>')

        else:
            return redirect('signIn')
    else:
        return render(request, 'uploadTemplate.html')


def template(request):
    if request.user.is_authenticated:

        tid = request.GET.get('id','')
        print(tid)
        uid = tid.split('_')[0]
        # print(uid)
        uploader = Users.objects.filter(id = uid).values_list('username')[0][0]
        # print(uploader)
        temp = Template.objects.filter(templateId = tid).values_list('description','date','totaldownloads')
        # print(temp)
        context = {
            'id': tid,
            'owner': uploader,
            'description': temp[0][0],
            'date': temp[0][1],
            'totdown': temp[0][2]
        }
        print(context)

        return render(request, 'template.html', context)
    else:
        return redirect('signIn')

# Edit user profile
def UpdateUserView(request):
    user = Users.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            profile = Users.objects.get(id=request.user.id)
            if form.cleaned_data['profile_img'] != profile.profile_img:
                # retrive old profile_img path and delete it from server
                profile.profile_img.delete(save=True)

            form.save()
            return redirect('home')

    return render(request, 'edituserProfile.html')

# Delete user profile
def DeleteUserProfile(request):
    templateData = Template.objects.filter(UID_id=request.user.id)

    if templateData:
        for row in templateData:
            imgpath = Path(f'static/templates/tempImages/{row.templateId}.jpg')
            filepath = Path(f'static/templates/tempFiles/{row.templateId}.zip')
            
            # to delete files
            if imgpath.exists():
                imgpath.unlink()
            if filepath.exists():
                filepath.unlink()
            
            # to delete rows from the database
            row.delete()

    request.user.profile_img.delete(save=True)
    request.user.delete()
    return redirect('signUp')
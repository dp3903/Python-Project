from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, LoginForm
from .models import Users
from templateData.models import Template
import os

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


def home(request):
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
                if os.path.isfile(imgpath + name +'.jpg'):
                    os.remove(imgpath + name +'.jpg')
                if os.path.isfile(imgpath + name +'.zip'):
                    os.remove(imgpath + name +'.zip')
                return HttpResponse('<h1>Template name already exists. Please try again with a different name.<h1>')
            except:
                if os.path.isfile(imgpath + name +'.jpg'):
                    os.remove(imgpath + name +'.jpg')
                if os.path.isfile(imgpath + name +'.zip'):
                    os.remove(imgpath + name +'.zip')
                return HttpResponse('<h1>Some error has occured. Please try again.</h1>')            
            print(temp)
            return HttpResponse('<h1>Successfully uploaded template...</h1>')

        else:
            return redirect('signIn')
    else:
        return render(request, 'uploadTemplate.html')
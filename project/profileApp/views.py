from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, LoginForm, EditUserProfileForm
from .models import Users
from templateData.models import Template,AppLogs
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
                newlog = AppLogs()
                newlog.transaction_type = "new"
                newlog.TID = None
                newlog.UID = Users.objects.filter(id = user.id)[0]
                # print(newlog)
                newlog.save()
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
        # print(context)

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
            uploadTemplates = Template.objects.filter(UID_id = request.user.id)
            downloadTemplateIds = AppLogs.objects.filter(transaction_type = "download", UID_id = request.user.id).values_list('TID_id',flat = True)
            # print(downloadTemplateIds)
            downloadTemplates = []
            for item in downloadTemplateIds:
                temp = Template.objects.filter(templateId = item)[0]
                downloadTemplates.append(temp)
            # print(downloadTemplates)
            
            # print(profileImg[0][0])
            # print(type(profileImg[0][0]))
            # print(profileImg[0][0] == '')
            context = {}
            if(profileImg[0][0] == ''):
                context = {
                    'profile' : 'profile.jpg',
                    'uploadTemplates' : uploadTemplates,
                    'downloadTemplates' : downloadTemplates
                }
            else:
                context = {
                    'profile' : profileImg[0][0][7:],
                    'uploadTemplates' : uploadTemplates,
                    'downloadTemplates' : downloadTemplates
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
                newlog = AppLogs()
                newlog.transaction_type = "upload"
                newlog.TID = Template.objects.filter(templateId = temp.templateId)[0]
                newlog.UID = Users.objects.filter(id = request.user.id)[0]
                print(newlog.transaction_type)
                print(newlog.TID)
                print(newlog.UID)
                newlog.save()
            except FileExistsError :
                return HttpResponse('<h1>Template name already exists. Please try again with a different name.<h1>')
            except Exception as error:
                print(error)
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
        profileImg = Users.objects.filter(username = request.user.username).values_list('profile_img')[0][0][7:]
        context = {
            'id': tid,
            'owner': uploader,
            'isowner': str(uid) == str(request.user.id),
            'profile' : profileImg,
            'description': temp[0][0],
            'date': temp[0][1],
            'totdown': temp[0][2]
        }
        # print(context)

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
            newlog = AppLogs()
            newlog.transaction_type = "update"
            newlog.TID = None
            newlog.UID = Users.objects.filter(id = request.user.id)[0]
            # print(newlog)
            newlog.save()
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


def download(request):
    if request.user.is_authenticated:
        tid = request.GET.get('Tid','')
        file_path = 'static/templates/tempFiles/' + tid + '.zip'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/.Zip")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                newlog = AppLogs()
                newlog.transaction_type = "download"
                newlog.TID = Template.objects.filter(templateId = tid)[0]
                newlog.UID = Users.objects.filter(id = request.user.id)[0]
                # print(newlog)
                newlog.save()
                temp = Template.objects.filter(templateId = tid)[0]
                temp.totaldownloads += 1
                temp.save()
                return response
        raise Http404
        # return redirect('home')
    else:
        return redirect('signIn')

def delete(request):
    if request.user.is_authenticated:
        tid = request.GET["tid"]
        imgpath = Path(f'static/templates/tempImages/{tid}.jpg')
        filepath = Path(f'static/templates/tempFiles/{tid}.zip')
            
        # to delete files
        if imgpath.exists():
            imgpath.unlink()
        if filepath.exists():
            filepath.unlink()

        temp = Template.objects.filter(templateId = tid)
        temp.delete()

        return redirect('home')

    return redirect('signIn')
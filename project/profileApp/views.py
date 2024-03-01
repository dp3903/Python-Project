from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, LoginForm
from .models import Users

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
            # upload logic
        else:
            return render(request, 'uploadTemplate.html')

    else:
        return render(request, 'uploadTemplate.html')
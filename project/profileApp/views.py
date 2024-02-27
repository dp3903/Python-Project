from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, LoginForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or another page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def sign_in(request):
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
        return render(request, 'home.html')
    else:
        return redirect('signIn')

def logout_request(request):
    logout(request)
    return redirect('signIn')

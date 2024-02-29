from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, LoginForm

def signUp(request):
    if request.method == 'POST':
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
                return render(request, 'signUp.html', {'username': username, 'email': email})
        else:
            return render(request, 'signUp.html', {'form': form})  # Pass form to template if form is invalid
    else:
        form = CustomUserCreationForm()
    return render(request, 'signUp.html', {'form': form})  # Pass form to template for initial rendering


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
        return render(request, 'home.html')
    else:
        return redirect('signIn')


def logout(request):
    logout(request)
    return redirect('signIn')

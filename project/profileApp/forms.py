# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
    profile_img = forms.ImageField()

    class Meta:
        model = Users
        fields = ('username', 'email', 'profile_img', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """RegisterForm definition."""
    # TODO: Define form fields here
    email = forms.EmailField()
    class Meta:
        model=User #USER DE DJANGO
        fields=['username','email','password1','password2']

class LoginForm(forms.Form):
    """LoginForm definition."""
    # TODO: Define form fields here
    #username
    username = forms.CharField(label="Username", max_length=200, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password
    password = forms.CharField(label="Password", max_length=200, required=True,widget=forms.PasswordInput(attrs={'class': 'form-control'}))


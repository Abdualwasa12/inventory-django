from django import forms
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','phone']
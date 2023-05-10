from typing import Any, Dict
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = CustomUser.objects.filter(username__iexact=username)
        if user.exists():
            raise forms.ValidationError("A user with that username already exists")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = CustomUser.objects.filter(email__iexact=email) 
        if user.exists():
            raise forms.ValidationError("A user with that email already exists") 
        return email
    
    


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
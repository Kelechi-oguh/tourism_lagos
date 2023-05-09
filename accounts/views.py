from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import SignUpForm, LoginForm

# Create your views here.

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        context = {"form": form}
        return render(request, 'signup.html', context=context)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign Up Succesful, Please Login!")
            return redirect('login')
        else:
            context = {"form": SignUpForm(), "error": "Form is not valid"}
            return render(request, 'signup.html', context)


class LogInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {"form": form}
        return render(request, 'login.html', context=context)
        
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
        messages.warning(request, "Invalid email or password.")
        return render(request, 'login.html', {"form": LoginForm()})



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home')
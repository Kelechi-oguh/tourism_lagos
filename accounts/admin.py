from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']
    

admin.site.register(CustomUser, CustomUserAdmin)
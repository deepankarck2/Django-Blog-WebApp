from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):   #inherits from creation form
    email = forms.EmailField()

    class Meta:
        model = User    #which model is going to be affected. Built in User model 
        fields = ['username', 'email', 'password1', 'password2']
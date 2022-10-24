from http.client import ImproperConnectionState
import imp
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #to show flash messages 

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')    #form info will save in cleaned_data dic after submitting


    else: 
        form = UserCreationForm()
    return render(request, 'Users/register.html', {'form': form})
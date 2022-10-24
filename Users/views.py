from http.client import ImproperConnectionState

from django.shortcuts import render
from django.shortcuts import redirect #to redirect users
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #to show flash messages 
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST': #buit in POST method
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #if valid, save user.
            username = form.cleaned_data.get('username')    #form info will save in cleaned_data dic after submitting
            messages.success(request, f'Account Created for {username}!') #showing flash success message
            return redirect('blog-home')
    else: 
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})
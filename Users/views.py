from http.client import ImproperConnectionState

from django.shortcuts import render
from django.shortcuts import redirect #to redirect users
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #to show flash messages 
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST': #buit in POST method
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #if valid, save user.
            username = form.cleaned_data.get('username')    #form info will save in cleaned_data dic after submitting
            messages.success(request, f'{username}, your account has been created') #showing flash success message
            return redirect('login')
    else: 
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

@login_required #DECORATOR: #need to make sure user is logged in before they can see their profile
def profile(request):   
    return render(request, 'Users/profile.html')
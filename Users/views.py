from http.client import ImproperConnectionState

from django.shortcuts import render
from django.shortcuts import redirect #to redirect users
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #to show flash messages 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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

    if request.method == 'POST':    #is user submits, then userinfo and picture is valid, then submit, show success message
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated') #showing flash success message
            return redirect('profile')  #https://youtu.be/CQ90L5jfldw?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p 
    else:
        u_form = UserUpdateForm(instance=request.user) #instanse is to populate username, and email
        p_form = ProfileUpdateForm(instance=request.user.profile) #inctanse is to populate

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'Users/profile.html', context)
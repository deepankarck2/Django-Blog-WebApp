from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#This is how we want to handle when an uses goes to the home page.
def home(request):  #takes a request argument, http response that we landed on the mohe page
    return HttpResponse('<h1>Blog Home</h1>')

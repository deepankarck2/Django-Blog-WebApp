#We want to pass which url to render what

from django.urls import path
from . import views #importing the views render folder


urlpatterns = [
    path('', views.home, name='blog-home'), #home page empty page, views.home returns the http responce 
    path('about/', views.about, name='blog-about'), 
]

"""Django_WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from re import template
from django.contrib import admin
from django.urls import path

from django.urls import include
from blog import views #it is to use our application(blog) file
from Users import views as user_views
from django.contrib.auth import views as auth_views #login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    #path('blog/', include('blog.urls')),   #if we go to blog, it will load blog pages/ map blog urls. Chop off the matched part, sends the left part. Like: blog/about, sends about/ 
    path('', include('blog.urls')), #empty to make the first page as home page

    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name='login'), #to use customized login page
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'), name='logout'), #to use customized logout page
]

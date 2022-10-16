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
from django.contrib import admin
from django.urls import path
from django.urls import include #it is to use our application(blog) file


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),   #if we go to blog, it will load blog pages/ map blog urls. Chop off the matched part, sends the left part. Like: blog/about, sends about/ 
]

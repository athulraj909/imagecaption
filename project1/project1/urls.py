"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),


    path('adminhome',views.adminhome,name='adminhome'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('adminuseraccept/<int:id>',views.adminuseraccept,name='adminuseraccept'),


    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('updat/<int:id>',views.updat, name='updat'),
    path('updat/updates/<int:id>',views.updates,name='updates'),
    path('userchangepassword',views.userchangepassword,name='userchangepassword'),
    path('uservision',views.uservision,name='uservision'),
]

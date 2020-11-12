"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from . import Views
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views
admin.site.site_header = "Krio.in"
admin.site.site_title = "Krio Admin Pannel"
admin.site.index_title = "Welcome to Krio Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.employeeList.as_view()),
    path('home',include('home.urls')),
    path('',Views.index,name="index"),
    path('features/',Views.features,name="index"),
    path('pricing/',Views.pricing,name="index"),
    
]

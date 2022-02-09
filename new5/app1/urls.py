"""new URL Configuration

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
from django.conf.urls import url

from app1 import views
app_name="app1"
urlpatterns = [

    url(r'^$', views.home, name="home"),
    url(r'^index/$', views.index, name="index"),

    url(r'list/$', views.studentlist, name="list"),
    url(r'form1/$', views.form1, name="form1"),
    url(r'form2/$', views.form2, name="form2"),
    url(r'form3/$', views.form3, name="form3"),
url(r'fact/$', views.fact, name="fact"),

]

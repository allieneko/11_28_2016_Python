"""integration_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.alloftheapps.urls', namespace = 'all')),
    url(r'^courses/', include('apps.courselist.urls', namespace = 'courses')),
    url(r'^ninja/', include('apps.disappearingninja.urls', namespace = 'ninja')),
    url(r'^register/', include('apps.loginreg.urls', namespace = 'register')),
    url(r'^gold/', include('apps.ninjagold2.urls', namespace = 'gold')),
    url(r'^survey/', include('apps.surveyform.urls', namespace = 'survey')),
]

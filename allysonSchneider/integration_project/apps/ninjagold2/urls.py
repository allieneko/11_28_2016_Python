from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^gold/process_money$', views.money, name = 'money'),
    url(r'^gold/refresh$', views.refresh, name = 'refresh')
]

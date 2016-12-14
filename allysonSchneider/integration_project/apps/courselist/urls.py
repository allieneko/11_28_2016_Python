from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^courses/addcourse$', views.addcourse, name = 'addcourse'),
    url(r'^courses/destroy/(?P<id>\d+)', views.confirm, name = 'confirm'),
    url(r'^courses/confirm/(?P<id>\d+)', views.destroy, name = 'destroy'),
    url(r'^courses/addstudent$', views.addstudent, name = 'addstudent')
]

from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register/register$', views.register, name = 'register'),
    url(r'^register/login$', views.login, name = 'login'),
    url(r'^register/delete/(?P<id>\d+)$', views.delete, name = 'delete')
]

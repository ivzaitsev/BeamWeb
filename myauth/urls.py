from django.conf.urls import patterns, url

from myauth import views

urlpatterns = patterns('',
                       url(r'^login', views.login, name='login'),
                       url(r'^register', views.register, name='register'),
)

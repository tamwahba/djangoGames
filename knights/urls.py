from django.conf.urls import patterns, url
from knights import views

urlpatterns = patterns('',
                       # /knights/registeruser
                       url(r'^registeruser/', views.registeruser, name='registeruser'),
                       # /knights/loginuser/
                       url(r'^loginuser/', views.loginuser, name='loginuser'),
                       # /knights/<user_name>/returnspriteinfo/
                       url(r'^(?P<user_name>[-A-Za-z0-9_]+)/returnspriteinfo/$', views.returnspriteinfo, name='returnspriteinfo'),
                       # /knights/highscores/
                       url(r'^highscores/', views.highscores, name='highscores'),
                       # /knights/<user_name>/updateuser/
                       url(r'^(?P<user_name>[-A-Za-z0-9_]+)/updateuser/', views.updateuser, name='updateuser'),
                       )

from django.conf.urls import url
from twitter import views
from django.views import generic
from . import views


urlpatterns = [url(r'^welcome$',views.welcome, name='welcome'),
                url(r'^welcomeUser$',views.welcomeUser, name='welcomeUser'),
                url(r'^timeline$',views.tweet, name='welcomeUser'),
                url(r'^deleteTweet$', views.deleteTweet, name='deleteTweet'),
               url(r'^', views.index, name='index'),


               ]


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('join', views.join, name="join"),
    path('create', views.create, name="create"),
    path('room', views.room, name="room"),
    path('error', views.error, name="error"),
    path('login', views.loginUser, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
]

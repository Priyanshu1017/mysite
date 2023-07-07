
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("index", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contacts", views.contacts, name='contacts'), 
    path("", views.signup, name='signup'), 
    path("user_login", views.user_login, name='user_login'), 
    path("user_logout", views.user_logout, name='user_logout'), 
]
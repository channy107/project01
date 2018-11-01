from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index', index),
    path('join', join, name ='join'),
    path('id_check', id_check, name='id_check'),
    path('login', login, name='login'),
]

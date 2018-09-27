#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       Administrator
   date：          2018-09-27
-------------------------------------------------
   Change Activity:
                   2018-09-27:
-------------------------------------------------
"""
__author__ = 'Administrator'
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    #path('login/', views.user_login,name='account_login' ),
    path('login/', auth_views.login,{"template_name": "account/login.html"},name='account_login' ),
    path('logout/', auth_views.logout,{"template_name": "account/logout.html"},name='account_logout'),
    path('register/', views.register,name='account_register'),
    path('password_change/',auth_views.password_change,
         {"template_name": "account/password_change.html","post_change_redirect":"password_change_done"}, name='password_change'),
    path('password_change_done/',auth_views.password_change_done,{"template_name": "account/password_change_done.html"}, name='password_change_done'),
]
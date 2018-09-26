#!/usr/bin python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       Administrator
   date：          2018-09-26
-------------------------------------------------
   Change Activity:
                   2018-09-26:
-------------------------------------------------
"""
__author__ = 'Administrator'

from django.urls import path, re_path
from  . import  views
urlpatterns = [
    path('blog_title/', views.blog_title),
    re_path('blog_title/(?P<article_id>[0-9]+)/', views.blog_article),
]
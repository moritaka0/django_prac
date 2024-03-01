#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:33:36 2019

@author: takahiromori
"""

from django.urls import path
from . import views
from django.conf.urls import url
#from .views import HelloView

urlpatterns = [
        #url(r'', HelloView.as_view(), name='index')
        path('',views.index, name='index'),
        path('card',views.cardWrite, name='card'),
        path('cardview',views.cardView, name='cardView'),
        path('regist',views.regist, name='regist'),
        path('show',views.cardShow, name='cardshow'),
        path('result',views.result, name='result'),
        #path('next',views.next, name='next')
]
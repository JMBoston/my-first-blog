# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:03:18 2018

@author: JohnM
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
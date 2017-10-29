#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt import views
from exp01.views import cust_auth

urlpatterns = [
    url(r'^token/$', views.obtain_jwt_token),
    url(r'^refresh/$', views.refresh_jwt_token),
    url(r'^verify/$', views.verify_jwt_token),
    url(r'^cust/$', cust_auth.CustViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)

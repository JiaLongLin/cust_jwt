#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import static
from rest_framework_jwt.views import JSONWebTokenAPIView

from exp01.views.serializers import JsonWebTokenSerializer


class CustViews(JSONWebTokenAPIView):

    serializer_class = JsonWebTokenSerializer

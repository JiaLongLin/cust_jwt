#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class JsonWebTokenSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(JsonWebTokenSerializer, self).__init__(*args, **kwargs)
        self.fields['username'] = serializers.CharField()
        self.fields['password'] = serializers.CharField(write_only=True)

    @property
    def object(self):
        return self.validated_data

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password')
        }
        if all(credentials.values()):
            user = authenticate(**credentials)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
                payload = jwt_payload_handler(user)
                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

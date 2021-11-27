#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:serializers.py
@time:2021/11/27
@email:tao.xu2008@outlook.com
@description:
"""
from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.models import Token

from .models import UserProfile


class TokenSerializer(serializers.ModelSerializer):
    """
    用户信息序列化
    """
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    phone = serializers.CharField(source="user.user.phone")
    email = serializers.CharField(source="user.email")
    date_joined = serializers.CharField(source="user.date_joined")

    class Meta:
        model = Token
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'phone', 'email', 'key', 'date_joined')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    扩展用户 信息序列化
    """
    user = UserSerializer()
    name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_name(self, obj):
        return obj.user.username


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        # token['username'] = user.username
        # token['code'] = 20000
        # print(token)
        # ... 官方示例中上面的部分没有生效
        # print(token)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        re_data = {'data': data, 'code': 200, 'message': 'success'}

        return re_data


if __name__ == '__main__':
    pass

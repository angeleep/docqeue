"""
 Code taken from https://www.section.io/engineering-education/api-authentication-with-django-knox-and-postman-testing/
"""
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from queueing.auth.auth import authenticate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')

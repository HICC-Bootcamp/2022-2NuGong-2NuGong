from django.contrib.auth.models import AbstractBaseUser
from rest_framework import serializers, validators
from . import models

class RegisterSerializer(serializers.Serializer):
    class Meta:
        model=AbstractBaseUser
        fields = ('name', 'password', 'department', 'favorites')
        
        extra_kwargs = {
            "password": {"write_only":True} #write_only를 통해 GET요청 시 접근을 차단
        }

    def create(self, validated_data):
        name = validated_data.get('name')
        password = validated_data.get('password')

        user = User.objects.create(
            name=name,
            password=password
        )

        return user
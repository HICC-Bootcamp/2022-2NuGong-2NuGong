from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializer import RegisterSerializer
from rest_framework.views import APIView


class CreateAccount(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(1111)
        print(user)
        print("not done")
        _, token = AuthToken.objects.create(user)

        print("done")
        return Response({
            'user_info': {
                'id': user.id,
                'nickname': user.nickname
            },
            "token": token
        })

class LoginAccount(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #username과 password가 옳지 않을 때 raise exception
        user = serializer.validated_data['user']

        _, token = AuthToken.objects.create(user)

        return Response({
            'user_info': {
                'id': user.id,
                'nickname': user.nickname
            },
            "token": token
        })
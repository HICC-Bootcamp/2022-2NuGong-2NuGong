from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializer import RegisterSerializer, UserInfoSerializer
from rest_framework.views import APIView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateAccountAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        _, token = AuthToken.objects.create(user)

        return Response({
            'user_info': {
                'id': user.id,
                'nickname': user.nickname
            },
            "token": token
        })

class LoginAccountAPI(APIView):
    permission_classes = [AllowAny]
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

class InfoAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # def post(self, request):
    #     # user = request.COOKIES
    #     # print(user)
    #     print(request)
    #     serializer = UserInfoSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response({'error': 'not authenticated'}, status=400)

    def put(self, request):
        serializer =UserInfoSerializer(request.user ,data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

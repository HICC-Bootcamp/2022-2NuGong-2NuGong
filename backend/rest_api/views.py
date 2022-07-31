from ast import Return
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from rest_framework.views import APIView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Notice
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.auth import AuthToken
from .serializer import RegisterSerializer, NoticeSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from datateam.recommendation import recommendation #recommendation.py에서 구현할 recommend 함수


class CreateAccountAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
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
            },
            status=status.HTTP_200_OK)
        except: 
            return Response(status=status.HTTP_404_NOT_FOUND)

class LoginAccountAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
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
            },
            status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserInfoAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
            try:
                user=User.objects.get(nickname=request.user)
                subscribe=user.subscribe
                clicked = dict(request.data)
                clickedTag = clicked["subscribe"]
                selectedDepartment = clicked["department"]
                #subscribe 수정
                for i in clickedTag:
                    index = int(i)
                    
                    if(subscribe[index] == 0):
                        subscribe[index] = 1
                    else:
                        subscribe[index] = 0

                user.subscribe = subscribe
                #department 수정
                user.department=int(selectedDepartment[0])
                user.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)


class NoticeListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.all().order_by('id')
        
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class NoticeDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    permission_classes = [AllowAny]
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.all().order_by('id')

    def viewIncrease(self, user_nickname, notice_id):
        tag = Notice.objects.get(id=notice_id).tag
        user=User.objects.get(nickname=user_nickname)
        favorites = user.favorites
        viewCount = favorites[tag]
        viewCount += 1
        favorites[tag] = viewCount
        user.favorites = favorites
        user.save()
        return 

    def get(self, request, *args, **kwargs):      
        try:
            notice_id = kwargs['pk']
            self.viewIncrease(request.user, notice_id)
            return self.retrieve(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class NoticeSearchAPI(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = NoticeSerializer

    def get_queryset(self):
        try:
            query = self.request.GET['query']
            return Notice.objects.filter(title__contains=query)
        except:
            department = self.request.GET['department']
            return Notice.objects.filter(department__contains=department)
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class NoticeSuggestionListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = NoticeSerializer

    def get_queryset(self):
        user = self.request.user
        recommended_list = recommendation(user.favorites)
        return Notice.objects.filter(tag__in=[11])
    
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class NoticeBookmarkAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny] #(IsAuthenticated,)  edit before release

    def put(self, request):
        try:
            user = self.request.user
            id = request.data["notice_id"]
            user.bookmarks.add(id)
            user.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self, request):
        try:
            user = self.request.user
            id = request.data["notice_id"]
            user.bookmarks.remove(id)
            user.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class NoticeBookmarkListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]
    serializer_class = NoticeSerializer

    def get_queryset(self):
        user = self.request.user
        return Notice.objects.filter(users__id__contains=user.id)

    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
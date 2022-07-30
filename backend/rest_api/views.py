from ast import Return
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bookmark, Notice
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializer import RegisterSerializer
from rest_framework.views import APIView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.auth import AuthToken
from .serializer import RegisterSerializer, BookmarkSerializer, NoticeSerializer
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework import mixins
from ..datateam.recommendation import recommend #recommendation.py에서 구현할 recommend 함수

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

class UserInfoAPI(APIView):
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
        return HttpResponse("successfully done")

class NoticeListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.all().order_by('id')
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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
        notice_id = kwargs['pk']
        self.viewIncrease(request.user, notice_id)
        return self.retrieve(request, *args, **kwargs)


class NoticeSearchAPI(generics.GenericAPIView, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = NoticeSerializer
    def get_queryset(self):
        query = self.request.GET['query']
        if query:
            return Notice.objects.filter(title__contains=query)
        else:
            return 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NoticeSuggestionListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        recommended_list = recommend(user.favorites)
        return Notice.objects.filter(tag__contained_by=recommended_list)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class NoticeBookmarkAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny] #(IsAuthenticated,)  edit before release
    def post(self, request):
        print(111)
        serializer = BookmarkSerializer(data=request.data)
        print(111)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        
        return HttpResponse("successfully done")

# class BookmarkListAPI(generics.GenericAPIView, mixins.ListModelMixin):
#     permission_classes = [AllowAny]
#     serializer_class = BookmarkSerializer
#     def get_queryset(self):
#         user = self.request.user
#         if user:
#             bookmarkList = Bookmark.objects.filter(user_id=user)
            
#         else:
#             return 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
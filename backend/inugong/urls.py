"""inugong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_api.views import NoticeListAPI, NoticeDetailAPI, NoticeSearchAPI, NoticeSuggestionListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('rest_api.urls')),
    path('notice/', NoticeListAPI.as_view()),
    path('notice/recommend/', NoticeSuggestionListAPI.as_view()),
    path('notice/<int:pk>/', NoticeDetailAPI.as_view()),
    path('search/', NoticeSearchAPI.as_view()),
]
from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('login/', views.LoginAccountAPI.as_view()),
    path('register/',views.CreateAccountAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
    path('info/', views.UserInfoAPI.as_view()),
    path('bookmark/', views.NoticeBookmarkAPI.as_view()),
    path('bookmark/list/', views.NoticeBookmarkListAPI.as_view()),
]

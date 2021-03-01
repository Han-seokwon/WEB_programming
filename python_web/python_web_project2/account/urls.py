
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# 앱 폴더의 views와 충돌을 피하기 위해 이름을 auth_views로 함
from . import views
app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html')
         , name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),


]
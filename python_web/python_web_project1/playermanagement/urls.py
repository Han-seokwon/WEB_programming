"""web_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views #  views.py import

app_name = 'playermanagement' # URL 패턴의 이름이 충돌하는 것을 방지하기 위한 namespace 역할
# 애플리케이션이 여러 개일 때 URL 패턴의 충동 방지

urlpatterns = [ # URL, 뷰 매핑
    path('', views.PlayerModelView.as_view(), name='index'),
    path('player/', views.PlayerList.as_view(), name='player_list'),
    path('team/', views.TeamList.as_view(), name='team_list'),
    path('player/<int:pk>', views.PlayerDetail.as_view(), name='player_detail'),
    path('team/<int:pk>', views.TeamDetail.as_view(), name='team_detail'),

]


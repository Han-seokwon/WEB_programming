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

app_name = 'survey' # URL 패턴의 이름이 충돌하는 것을 방지하기 위한 namespace 역할
# 애플리케이션이 여러 개일 때 URL 패턴의 충동 방지

urlpatterns = [ # URL, 뷰 매핑
    path('', views.IndexView.as_view(), name= 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('name/', views.get_name, name='name'),
    path('name/name_list/', views.show_nameList, name='name_list'),
]

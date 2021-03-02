
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'bulletin'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('answer/create/<int:pk>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

]

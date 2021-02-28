from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Player, Team

class PlayerModelView(TemplateView):
    template_name = 'playermanagement/index.html'

    def get_context_data(self, **kwargs):
        # get_context_data를 정의할 때는 첫 줄에 super 메소드를 호출해야함
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Player', 'Team']

        return context

class PlayerList(ListView):
    model = Player
    # object_list 컨텍스트 변수 구성
    # 템플릿 파일은 디폴트로 모델명(소문자)_list.html 형식; 여기서는 player_list.html

class TeamList(ListView):
    model = Team

class PlayerDetail(DetailView):
    model = Player
    # object로 컨텍스트 변수 구성; URLconf로부터 Primary ket(pk) 값을 받아 DB 레코드를 조회함
    # 템플릿 파일은 디폴트로 모델명(소문자)_list.html 형식; 여기서는 player_detail.html

class TeamDetail(DetailView):
    model = Team
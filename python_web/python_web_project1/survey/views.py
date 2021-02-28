from django.shortcuts import get_object_or_404, render # 장고의 shortcut function 단축함수
from .models import Question, Choice, NameList # models.py의 Question, Choice 클래스 import
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse # django.core.urlresolvers 모듈은 삭제됨
from .form import nameForm
from django.views.generic import ListView, DetailView
import logging

# survey.views 로거 객체를 취득; 객체 이름 survey.views
# 로거의 부모인 survey로 로그 레코드(= 로그 메시지)가 전파됨(survey 로거는 settings.py에서 정의함)
# survey 로거에서 메시지 기록
logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'survey/index.html'
    # 컨텍스트 변수명 지정
    context_object_name = 'lastest_question_list'
    def get_queryset(self):
        # pub_date를 역순으로 했을 때 5개의 항목만 반환
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'survey/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'survey/results.html'



def vote(request, question_id):
    # debug() 메소드를 통해 DEBUG 로그 레벨의 로그 메시지를 생성함
    # 로거는 file 핸들러를 사용해 해당 log 파일에 로그 메시지 기록
    logger.debug("vote().question_id: %s" % question_id)

    question = get_object_or_404(Question, pk = question_id)
    try:
        # Choice 테이블을 pk=request.POST['choice'] 검색조건으로 검색
        # request.POST['choice']는 폼 데이터에서 key가 choice에 해당하는 값인 choice.id를 스트링으로 리턴
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # except 발생시 question과 에러메시지 컨텍스트를 detail.html 템플릿에 전달하여 에러 메시지와 함께 질문 항목을 다시 보여줌
        context={ 'question' : question, 'error_message' : "You didn't select a choice"}
        return render(request, 'survey/detail.html', context)

    else: # except 발생 안 한 경우
        selected_choice.votes += 1 # Choice 객체.votes 선택 카운트 +1
        selected_choice.save() # 변경사항을 Choice 테이블에 저장
        #  Redirect할 URL을 담은 HttpResponseRedirect 객체 반환
        # reverse 함수로 URL 추출
        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/results.html', {'question' : question})

def get_name(request):
    # POST 방식이면, 데이터가 담긴 제풀된 폼으로 간주
    if request.method == 'POST':
        # request에 담긴 데이터로 클래스 폼 생성; 바운드 폼
        form = nameForm(request.POST)

        # 폼에 담긴 데이터의 유효성 검사
        if form.is_valid():
            entered_name = form.cleaned_data['enter_name']
            name_instance = NameList(name = entered_name)
            name_instance.save()
            # 리다이렉션
            return HttpResponseRedirect('name_list/')

    # GET 방식이면, 빈 폼을 보여줌
    else:
        form = nameForm()

    return render(request, 'survey/name.html', {'form' : form})


def show_nameList(request):
    list_of_name = NameList.objects.all()
    context = {'list_of_name' : list_of_name}
    return render(request , 'survey/name_list.html', context)





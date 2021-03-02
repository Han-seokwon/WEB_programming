from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, Subject
from django.views import generic 
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import  Paginator
from my_module import pagination
from django.contrib.auth.decorators import login_required


def index(request):

    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')

    # 한 페이지에 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    page_range_by10 = pagination.pagination_by10(int(page))
    context = {'question_list': page_obj, 'page_range' : page_range_by10}

    # 페이지 표시 제한 10개씩,

    return render(request, 'bulletin/question_list.html', context)

# class IndexView(generic.ListView):
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')

class DetailView(generic.DetailView):
    model = Question



@login_required(login_url='account:login')
def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)

            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('bulletin:detail', pk=question.id)
    else:
        form = AnswerForm()

    return render(request, 'bulletin/question_detail.html',
                  {'question': question, 'form': form})

@login_required(login_url='account:login')
def question_create(request):
    # POST 요청 방식인 경우; form에서 사용자가 질문을 작성하고 저장하기를 누른 경우
    if request.method == 'POST':
        subject = request.POST.getlist('subject')
        form = QuestionForm(request.POST)

        # form.is_valid() : 폼이 유효하지 않으면 폼에 오류가 저장되어 사용자에게 보여줌
        if form.is_valid():
            # 임시저장
            question = form.save(commit = False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('bulletin:index')

    # GET 요청 방식인 경우; index에서 질문 등록하기를 눌러 처음 form에 들어왔을 때
    else:
        form = QuestionForm()

    subject_list = Subject.objects.all()


    return render(request, 'bulletin/question_form.html',
              {'form' : form, 'subject_list' : subject_list
             })

















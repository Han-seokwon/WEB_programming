from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','subject', 'content']
        # 모든 필드를 선택
        # fields = '__all__'

        widgets = {
            'subject': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': '제목',
            'subject': '분야',
            'content': '내용',
        }

        error_messages={
            'title' : {'required' : '제목을 입력해주세요.'},
            'subject': {'required' : '항목을 하나 이상 선택해주세요.'},
            'content': {'required' : '내용을 입력해주세요.'},
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

        error_messages = {
            'content': {'required' : '답변 내용을 입력해주세요.'},
        }


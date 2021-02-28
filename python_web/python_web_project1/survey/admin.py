from django.contrib import admin
from .models import Question, Choice, NameList # model.py에서 정의한 클래스 import
# Register your models here.


class ChoiceInline(admin.StackedInline):
    model = Choice
    # 한 번에 보여줄 Choice_text 개수
    extra = 3


class Question_admin(admin.ModelAdmin):
    # 필드 순서 변경
    # fields = [ 'pub_date', 'question_text']

    # 필드 분리; (필드 제목 , {key(반드시 fields이어야 함): 클래스 변수이름})
    # fieldsets = [ ('Question Statement', {'fields' : ['question_text']})
    #               , ('Date Information', {'fields' : ['pub_date']})]

    # 필드 접기
    # fieldsets = [ ('Question Statement', {'fields' : ['question_text']})
    #               , ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']})]# 접어진 필드

    # Choice 모델 클래스 같이 보기
    fieldsets = [(None, {'fields': ['question_text']})
                 , ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']})]
    inlines = [ChoiceInline]
    list_display = ('question_text' ,'pub_date') # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date'] # 필터 사이드 바 추가 list or tuple
    search_fields = ['question_text'] # 검색 박스 추가



# model.py에서 정의한 클래스를 Admin 사이트에 등록
admin.site.register(Question, Question_admin)
admin.site.register(Choice)
admin.site.register(NameList)
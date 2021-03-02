from django.contrib import admin
from .models import Question, Answer, Subject

class QuestionAdmin(admin.ModelAdmin):
        search_fields = ['title']

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Subject)


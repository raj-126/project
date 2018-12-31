from django.contrib import admin
from .models import Question,answer

class QuestionView(admin.ModelAdmin):
    list_display = ['question_text','question_text1']
    list_filter = ['question_text','question_text1']

class AnswerView(admin.ModelAdmin):
    list_display = ['choice_text','votes']
    list_filter = ['choice_text','votes']
    
admin.site.register(Question,QuestionView)
admin.site.register(answer,AnswerView)



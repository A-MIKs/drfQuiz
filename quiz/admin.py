from django.contrib import admin
from .models import *

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ["answer_text", "is_right"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineModel]
    fields = ["title", "quiz"]
    list_display = ["title", "quiz", "updated"]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer_text", "is_right", "question"]
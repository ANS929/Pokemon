from django.contrib import admin
from .models import Quiz, CompletedQuiz, Practice, CompletedPractice, Student

admin.site.register(Quiz)
admin.site.register(Practice)
# admin.site.register(Course)

@admin.register(CompletedQuiz)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_completed')
    search_fields = ('student__username', 'quiz__title')

@admin.register(CompletedPractice)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'practice','date_completed')

@admin.register(Student)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
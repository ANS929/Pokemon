from django.contrib import admin
from .models import Quiz, CompletedQuiz, Practice, CompletedPractice, Student, Course, RegisteredStudent

admin.site.register(Course)
admin.site.register(RegisteredStudent)

@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level',)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level',)

@admin.register(CompletedQuiz)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_completed')
    search_fields = ('student__username', 'quiz__title')

@admin.register(CompletedPractice)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'practice', 'date_completed')

@admin.register(Student)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
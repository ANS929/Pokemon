from django.contrib import admin
from .models import Quiz, CompletedQuiz, Practice, CompletedPractice, Student, Course, RegisteredStudent, Child, RegisteredChild, Badge, CompletedBadge, Unit, GradeLevel, CompletedUnit

admin.site.register(Course)
admin.site.register(RegisteredStudent)
admin.site.register(Child)
admin.site.register(RegisteredChild)
admin.site.register(CompletedBadge)

@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level', 'unit')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level', 'unit')

@admin.register(CompletedQuiz)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_completed', 'perfect_score')
    search_fields = ('student__username', 'quiz__title')

@admin.register(CompletedPractice)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'practice', 'date_completed')

@admin.register(Student)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Unit)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level')

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CompletedUnit)
class CompletedUnitAdmin(admin.ModelAdmin):
    list_display = ('student', 'unit', 'date_completed')
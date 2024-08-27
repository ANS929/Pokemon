from django.contrib import admin
from .models import Quiz, CompletedQuiz, Practice, CompletedPractice, Student, Course, RegisteredStudent, Child, RegisteredChild, Badge, CompletedBadge, Unit, GradeLevel, CompletedUnit, EnrolledStudent

admin.site.register(Course)
admin.site.register(RegisteredStudent)
admin.site.register(Child)
admin.site.register(RegisteredChild)
admin.site.register(EnrolledStudent)

@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level', 'unit')

@admin.register(CompletedPractice)
class CompletedPracticeAdmin(admin.ModelAdmin):
    list_display = ('student', 'practice', 'date_completed')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade_level', 'unit')

@admin.register(CompletedQuiz)
class CompletedQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date_completed', 'perfect_score')
    search_fields = ('student__username', 'quiz__title')

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CompletedBadge)
class CompletedBadgeAdmin(admin.ModelAdmin):
    list_display = ('student', 'badge', 'date_completed')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level')

@admin.register(CompletedUnit)
class CompletedUnitAdmin(admin.ModelAdmin):
    list_display = ('student', 'unit', 'date_completed')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
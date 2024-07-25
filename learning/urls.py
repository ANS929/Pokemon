from django.urls import path
from learning import views

app_name = 'learning'

urlpatterns = [
    path('', views.learning_home, name='learning_home'),
    
    # student paths
    path('students/', views.students, name='students'),
    path('students/dashboard/<int:user_id>/', views.student_dashboard, name='student_dashboard'),
    path('students/gr1/', views.gr1, name='gr1'),
    path('students/gr2/', views.gr2, name='gr2'),
    path('students/gr3/', views.gr3, name='gr3'),
    path('students/gr4/', views.gr4, name='gr4'),
    path('students/gr5/', views.gr5, name='gr5'),
    path('students/gr6/', views.gr6, name='gr6'),
    path('students/gr7/', views.gr7, name='gr7'),
    path('students/gr8/', views.gr8, name='gr8'),
    path('students/gr4/unit/<slug:unit_slug>/', views.unit_detail, name='unit_detail'),
    path('students/gr4/quiz/<slug:quiz_slug>/', views.quiz_detail, name='quiz_detail'),
    path('students/gr4/practice/<slug:practice_slug>/', views.practice_detail, name='practice_detail'),
    path('students/gr4/quiz/<slug:quiz_slug>/submit/', views.submit_quiz, name='submit_quiz'),
    path('students/gr4/quiz/<slug:quiz_slug>/explanations/', views.quiz_explanations, name='quiz_explanations'),
    path('students/gr4/practice/<slug:practice_slug>/submit/', views.submit_practice, name='submit_practice'),
    
    # teacher paths
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teachers/dashboard/add_student/', views.add_student, name='add_student'),
    path('teachers/dashboard/remove_student/', views.remove_student, name='remove_student'),
    path('teachers/dashboard/class/new/', views.new_course, name='new_class'),
    path('teachers/dashboard/class/<int:course_id>/', views.view_course, name='view_class'),
    path('teachers/dashboard/class/<int:course_id>/edit/', views.edit_course, name='edit_class'),
    path('teachers/dashboard/class/<int:course_id>/delete/', views.delete_course, name='delete_class'),
    path('teachers/dashboard/class/<int:course_id>/enroll/', views.enroll_student, name='enroll_student'),
    path('teachers/dashboard/class/<int:course_id>/unenroll/<int:student_id>/', views.unenroll_student, name='unenroll_student'),

    # parent paths
    path('parents/', views.parents, name='parents'),
    path('parents/dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('parents/dashboard/add_child/', views.add_child, name='add_child'),
    path('parents/dashboard/remove_child/', views.remove_child, name='remove_child'),
]
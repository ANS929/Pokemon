from django.urls import path
from learning import views

app_name = 'learning'

urlpatterns = [
    path('', views.learning_home, name='learning_home'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('parents/', views.parents, name='parents'),
    path('parents/dashbaord', views.parent_dashboard, name='parent_dashboard'),
    path('teachers/dashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('teachers/dashboard/your_classes', views.your_classes, name='your_classes'),
    path('teachers/dashboard/your_students', views.your_students, name='your_students'),
    path('parents/dashboard/your_children', views.your_children, name='your_children'),
    path('students/gr1', views.gr1, name='gr1'),
    path('students/gr2', views.gr2, name='gr2'),
    path('students/gr3', views.gr3, name='gr3'),
    path('students/gr4', views.gr4, name='gr4'),
    path('students/gr5', views.gr5, name='gr5'),
    path('students/gr6', views.gr6, name='gr6'),
    path('students/gr7', views.gr7, name='gr7'),
    path('students/gr8', views.gr8, name='gr8'),
    path('students/dashboard', views.student_dashboard, name='student_dashboard'),
    path('students/gr4/comparing_whole_numbers', views.comparing_whole, name='comparing_whole'),
    path('students/gr4/comparing_decimals', views.comparing_decimal, name='comparing_decimal'),
    path('students/gr4/addition_subtraction', views.add_subtract, name='add_subtract'),
    path('students/gr4/multiplication', views.multiplication, name='multiplication'),
    path('students/gr4/realworld_whole_numbers', views.rw_whole, name='rw_whole'),
    path('students/gr4/realworld_fractions', views.rw_fraction, name='rw_fraction'),
    path('students/gr4/symmetry', views.symmetry, name='symmetry'),
    path('students/gr4/identifying_shapes', views.identifying_shapes, name='identifying_shapes'),
    path('students/gr4/converting_units', views.converting_units, name='converting_units'),
    path('students/gr4/area_perimeter', views.area_perimeter, name='area_perimeter'),
    path('students/gr4/representing_data', views.representing, name='representing'),
    path('students/gr4/interpreting_data', views.interpreting, name='interpreting'),
    path('students/gr4/<slug:quiz_slug>/', views.quiz_detail, name='quiz_detail'),
    path('students/gr4/<slug:quiz_slug>/submit/', views.submit_quiz, name='submit_quiz'),
]
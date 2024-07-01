from django.urls import path
from learning import views

app_name = 'learning'

urlpatterns = [
    path('', views.learning_home, name='learning_home'),
    path('students/', views.students_home, name='students_home'),
    path('teachers/', views.teachers, name='teachers'),
    path('parents/', views.parents, name='parents'),
    path('teachers/classes', views.classes, name='classes'),
    path('teachers/students', views.students, name='students'),
    path('parents/children', views.children, name='children'),
    path('students/gr1', views.gr1, name='gr1'),
    path('students/gr2', views.gr2, name='gr2'),
    path('students/gr3', views.gr3, name='gr3'),
    path('students/gr4', views.gr4, name='gr4'),
    path('students/gr5', views.gr5, name='gr5'),
    path('students/gr6', views.gr6, name='gr6'),
    path('students/gr7', views.gr7, name='gr7'),
    path('students/gr8', views.gr8, name='gr8'),
    path('students/dashboard', views.dashboard, name='dashboard'),
    path('students/gr4/comparing_whole_numbers', views.comparing_whole, name='comparing_whole'),
    path('students/gr4/comparing_decimals', views.comparing_decimal, name='comparing_decimal'),
    path('students/gr4/addition_subtraction', views.add_subtract, name='add_subtract'),
    path('students/gr4/multiplication', views.multiplication, name='multiplication'),
    path('students/gr4/realworld_whole_numbers', views.rw_whole, name='rw_whole'),
    path('students/gr4/realworld_fractions', views.rw_fraction, name='rw_fraction'),
    path('students/gr4/symmetry', views.symmetry, name='symmetry'),
    path('students/gr4/classifying_shapes', views.classifying_shapes, name='classifying_shapes'),
    path('students/gr4/converting_units', views.converting_units, name='converting_units'),
    path('students/gr4/area_perimeter', views.area_perimeter, name='area_perimeter'),
    path('students/gr4/representing_data', views.representing, name='representing'),
    path('students/gr4/interpreting_data', views.interpreting, name='interpreting'),
    path('students/gr4/number_sense_quiz', views.ns_quiz, name='ns_quiz'),
]
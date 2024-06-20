from django.urls import path
from education import views

app_name = 'education'

urlpatterns = [
    path('', views.education_home, name='education_home'),
]

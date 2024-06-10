from django.urls import path
from education import views

app_name = 'education'

urlpatterns = [
    path('', views.index, name='index'),
]

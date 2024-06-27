from django.urls import path
from learning import views

app_name = 'learning'

urlpatterns = [
    path('', views.learning_home, name='learning_home'),
]

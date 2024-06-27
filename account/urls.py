from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('', views.account_home, name='account'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
]
from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    # path('login/', views.user_login, name='login'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.user_logout, name='logout'),
    path('settings/', views.settings, name='settings'),  
]
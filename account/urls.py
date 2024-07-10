from django.urls import path, include
from . import views
from .views import CustomRegistrationView

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    path('register/', CustomRegistrationView.as_view(), name='registration_register'),
    path('register/complete', views.registration_complete, name='registration_complete'),
    path('settings/', views.settings, name='settings'),
    # path('login/', views.user_login, name='login'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.user_logout, name='logout'),
]
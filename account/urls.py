from django.urls import path, include
from . import views
from .views import custom_registration_view

app_name = 'account'

urlpatterns = [

    # registration
    path('register/', custom_registration_view.as_view(), name='registration_register'),
    path('register/complete/', views.registration_complete, name='registration_complete'),

    # profile
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
]
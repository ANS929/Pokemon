from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community'),
]
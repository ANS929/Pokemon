from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community'),
    path('maths/', views.maths_forum, name='maths_forum'),
    path('tcg/', views.tcg_forum, name='tcg_forum'),

]
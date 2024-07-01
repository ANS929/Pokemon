from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community'),
    path('math/', views.math_forum, name='math_forum'),
    path('tcg/', views.tcg_forum, name='tcg_forum'),

]

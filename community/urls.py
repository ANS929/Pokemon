from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community'),
    path('math/', views.MathQuestionListView.as_view(), name='math_forum'),
    path('tcg/', views.TCGQuestionListView.as_view(), name='tcg_forum'),
    path('math/<int:pk>/', views.MathQuestionDetailView.as_view(), name='math_question_details'),
    path('tcg/<int:pk>/', views.TCGQuestionDetailView.as_view(), name='tcg_question_details'),
]
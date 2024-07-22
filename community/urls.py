from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community'),

    # math forum
    path('math/', views.MathQuestionListView.as_view(), name='math_forum'),
    path('math/create/', views.MathQuestionCreateView.as_view(), name='math_question_create'),
    path('math/<int:pk>/', views.MathQuestionDetailView.as_view(), name='math_question_details'),
    path('math/<int:pk>/update/', views.MathQuestionUpdateView.as_view(), name='math_question_update'),
    path('math/<int:pk>/delete/', views.MathQuestionDeleteView.as_view(), name='math_question_delete'),
    path('math/<int:pk>/comment/', views.AddMathCommentView.as_view(), name='math_question_comment'),

    # tcg forum
    path('tcg/', views.TCGQuestionListView.as_view(), name='tcg_forum'),
    path('tcg/create/', views.TCGQuestionCreateView.as_view(), name='tcg_question_create'),
    path('tcg/<int:pk>/', views.TCGQuestionDetailView.as_view(), name='tcg_question_details'),
    path('tcg/<int:pk>/update/', views.TCGQuestionUpdateView.as_view(), name='tcg_question_update'),
    path('tcg/<int:pk>/delete/', views.TCGQuestionDeleteView.as_view(), name='tcg_question_delete'),
    path('tcg/<int:pk>/comment/', views.AddTCGCommentView.as_view(), name='tcg_question_comment'),
]
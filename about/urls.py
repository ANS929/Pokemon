from django.urls import path
from about import views

app_name = 'about'

urlpatterns = [
    path('', views.about_home, name='about'),
    path('site/', views.site, name='site'),
    path('tcg/', views.tcg, name='tcg'),
    path('tcg/quickstart/', views.quickstart, name='quickstart')
]
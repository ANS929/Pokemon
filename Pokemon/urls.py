from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from learning import views as learning_views
from about import views as about_views
from account import views as account_views
from community import views as community_views

urlpatterns = [
    path('', learning_views.index, name='index'),
    path('learning/', include('learning.urls')),
    path('account/', include('account.urls')),
    path('about/', include('about.urls')),
    path('community/', include('community.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

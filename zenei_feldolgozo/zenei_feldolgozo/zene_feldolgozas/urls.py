from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'zene_feldolgozas'

urlpatterns = [
    path('', views.index, name='index'),
    path('feldolgozas/', views.process_audio_view, name='feldolgozas'),
    path("process_audio", views.process_audio_view, name="process_audio"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "collected_static")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
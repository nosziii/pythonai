from django.urls import path
from . import views

app_name = 'zene_feldolgozas'

urlpatterns = [
    path('', views.index, name='index'),
    path('feldolgozas/', views.process_audio_view, name='feldolgozas'),
    path("process_audio", views.process_audio_view, name="process_audio"),
]

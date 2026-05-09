from django.urls import path
from . import views

urlpatterns = [
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('', views.index, name='index'),
    path('que-es-aplv/', views.que_es_aplv, name='que_es_aplv'),
    path('sintomas/', views.sintomas, name='sintomas'),
    path('alternativas/', views.alternativas, name='alternativas'),
    path('diagnostico/', views.diagnostico, name='diagnostico'),
    path('alimentos/', views.alimentos, name='alimentos'),
    path('recetas/', views.recetas, name='recetas'),
    path('directorio/', views.directorio, name='directorio'),
    path('apoyo/', views.apoyo, name='apoyo'),
]

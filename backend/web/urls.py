from django.urls import path
from . import views

urlpatterns = [
    # SEO & Base URLs
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('', views.index, name='index'),

    # Sitemap Oficial / Nuevas URLs
    path('alergias/', views.que_es_aplv, name='alergias'),
    path('alergias/sintomas/', views.sintomas, name='sintomas'),
    path('alergias/tipos/', views.tipos, name='tipos'),
    path('etiquetas/', views.etiquetas, name='etiquetas'),
    path('formulas/', views.alternativas, name='formulas'),
    path('recetas/', views.recetas, name='recetas'),
    path('escuelas/', views.escuelas, name='escuelas'),
    path('familia/', views.familia, name='familia'),
    path('comunidad/', views.comunidad, name='comunidad'),
    path('escaner/', views.escaner, name='escaner'),
    path('contacto/', views.directorio, name='contacto'),

    # Compatibilidad (para prevenir roturas con urls antiguas en templates existentes)
    path('que-es-aplv/', views.que_es_aplv, name='que_es_aplv'),
    path('alternativas/', views.alternativas, name='alternativas'),
    path('diagnostico/', views.diagnostico, name='diagnostico'),
    path('alimentos/', views.alimentos, name='alimentos'),
    path('directorio/', views.directorio, name='directorio'),
    path('apoyo/', views.apoyo, name='apoyo'),
]

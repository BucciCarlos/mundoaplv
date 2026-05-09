from django.shortcuts import render

from django.http import HttpResponse

def robots_txt(request):
    """View for robots.txt."""
    return render(request, 'robots.txt', content_type="text/plain")

def index(request):
    """View for the landing page."""
    return render(request, 'index.html')

def que_es_aplv(request):
    """View for the 'What is CMPA?' page."""
    return render(request, 'que-es-aplv.html')

def sintomas(request):
    """View for the Symptoms page."""
    return render(request, 'sintomas.html')

def alternativas(request):
    """View for the Alternatives page."""
    return render(request, 'alternativas.html')

def diagnostico(request):
    """View for the Diagnosis page."""
    return render(request, 'diagnostico.html')

def alimentos(request):
    """View for the Allowed Foods page."""
    return render(request, 'alimentos.html')

def recetas(request):
    """View for the Recipes page."""
    return render(request, 'recetas.html')

def directorio(request):
    """View for the Medical Directory page."""
    return render(request, 'directorio.html')

def apoyo(request):
    """View for the Support Group page."""
    return render(request, 'apoyo.html')

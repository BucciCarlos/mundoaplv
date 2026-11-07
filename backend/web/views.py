from django.shortcuts import render

from django.http import JsonResponse


def health_check(request):
    """Minimal process health check without external dependencies."""
    return JsonResponse({'status': 'ok'})

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

def tipos(request):
    """View for the Types of Allergy page."""
    return render(request, 'tipos.html')

def etiquetas(request):
    """View for the Labels guide page."""
    return render(request, 'etiquetas.html')

def escuelas(request):
    """View for the Schools/Educators page."""
    return render(request, 'escuelas.html')

def familia(request):
    """View for the Family and Caregivers page."""
    return render(request, 'familia.html')

def comunidad(request):
    """View for the Community forum page."""
    return render(request, 'comunidad.html')

def escaner(request):
    """View for the Product Scanner page."""
    return render(request, 'escaner.html')

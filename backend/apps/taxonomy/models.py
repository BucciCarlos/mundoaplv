from django.db import models

class Allergen(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    caa_hidden_names = models.TextField(
        blank=True,
        help_text="Nombres ocultos o derivados en etiquetas según el Código Alimentario Argentino"
    )

    def __str__(self):
        return self.name

class Allergy(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_ige_mediated = models.BooleanField(default=False)
    allergens = models.ManyToManyField(Allergen, related_name='allergies')

    def __str__(self):
        return self.name

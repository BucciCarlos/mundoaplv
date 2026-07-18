from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    instructions = models.TextField()
    prep_time_minutes = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    contains_allergens = models.ManyToManyField(
        'taxonomy.Allergen',
        related_name='recipes',
        help_text="Alérgenos presentes en esta receta (se utilizarán para exclusión en búsquedas)"
    )

    def __str__(self):
        return self.title

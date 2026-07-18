from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    instructions = models.TextField()
    prep_time_minutes = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    free_from_allergens = models.ManyToManyField(
        'taxonomy.Allergen',
        related_name='safe_recipes',
        help_text="Alérgenos de los cuales esta receta está libre"
    )

    def __str__(self):
        return self.title

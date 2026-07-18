from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('MEDICAL', 'Médico/Científico'),
        ('LEGAL', 'Leyes/Normativas'),
        ('SCHOOL', 'Escuelas/Instituciones'),
        ('FAMILY', 'Familiar/Apoyo'),
        ('GENERAL', 'General/Informativo'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='GENERAL'
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

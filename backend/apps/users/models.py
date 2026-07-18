from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('PARENT', 'Padre / Tutor'),
        ('FAMILY', 'Familiar / Cuidador'),
        ('EDUCATOR', 'Institución Educativa / Docente'),
        ('ADMIN', 'Administrador'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='PARENT'
    )
    country = models.CharField(
        max_length=2,
        default='AR'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

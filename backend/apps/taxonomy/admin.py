from django.contrib import admin
from .models import Allergen, Allergy

@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'caa_hidden_names')

@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_ige_mediated')
    filter_horizontal = ('allergens',)
    search_fields = ('name',)
    list_filter = ('is_ige_mediated',)

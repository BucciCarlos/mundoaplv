from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'prep_time_minutes', 'is_published')
    list_filter = ('is_published', 'contains_allergens')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('contains_allergens',)
    search_fields = ('title', 'instructions')

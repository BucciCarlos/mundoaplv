from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = UserAdmin.list_display + ('role', 'country')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Información de APLV', {'fields': ('role', 'country')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de APLV', {'fields': ('role', 'country')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import DonaCafeteria, Cafeteria
from django.contrib.auth.admin import UserAdmin

class DonaCafeteriaAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'foto_perfil']

    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos', {'fields':('foto_perfil', 'bio')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {'fields':('foto_perfil', 'bio')}),
    )

admin.site.register(Cafeteria)
admin.site.register(DonaCafeteria, DonaCafeteriaAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAbs

admin.site.register(UserAbs)

class UserAbsAdmin(UserAdmin):
    list_display = ('username', 'email', 'biografia','idade','telefone', 'endereco','escolaridade', 'qtd_animais', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('biografia','idade','telefone', 'endereco','escolaridade', 'qtd_animais')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('biografia','idade','telefone', 'endereco','escolaridade', 'qtd_animais')}),
    )
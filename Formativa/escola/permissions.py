from rest_framework import permissions

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Gestor').exists()

# class IsGestor(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Leitura (GET, HEAD, OPTIONS) liberada para quem estiver autenticado
#         if request.method in permissions.SAFE_METHODS:
#             return request.user and request.user.is_authenticated
#         # Escrita (POST, PUT, DELETE) apenas para gestores
#         return request.user.groups.filter(name='Gestores').exists()

from rest_framework import permissions

from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Gestor').exists()

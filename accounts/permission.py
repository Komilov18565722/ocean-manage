from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user and request.user.type == 'manager'

    def has_object_permission(self, request, view, obj):
        return True
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка, является ли пользователь владельцем модуля"""
    message = 'Вы не являетесь владельцем'

    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True
        return False

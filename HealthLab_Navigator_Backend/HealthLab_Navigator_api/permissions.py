from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет чтение для всех, но требует суперпользователя для изменения.
    """

    def has_permission(self, request, view):
        # Разрешение для всех для метода GET
        if request.method in permissions.SAFE_METHODS:
            return True
        # Требуется суперпользователь для остальных методов
        return request.user and request.user.is_superuser


class MedicalAgentPermission(permissions.BasePermission, ):
    """
    Разрешение, которое позволяет чтение для всех, но требует медицинского агента для изменения только
     для медицинских учреждений, филиалов и других объектов, подвластных ему.
    """
    def has_permission(self, request, view):
        # Разрешение для всех для метода GET
        if request.method in permissions.SAFE_METHODS:
            return True
        # Требуется медицинский агент для остальных методов
        return request.user and request.user.is_medical_agent


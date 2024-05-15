from rest_framework import permissions
from .models import MedicalAgentOfMedicalInstitution


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


class MedicalInstitutionPermission(permissions.BasePermission, ):
    def has_permission(self, request, view):
        # Разрешение для всех для метода GET
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and MedicalAgentOfMedicalInstitution.objects.filter(user=request.user).exists():
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if MedicalAgentOfMedicalInstitution.objects.filter(user=request.user, medical_institution=obj).exists():
            return True
        return False


class MedicalInstitutionBranchPermission(permissions.BasePermission, ):
    def has_permission(self, request, view):
        # Разрешение для всех для метода GET
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and MedicalAgentOfMedicalInstitution.objects.filter(user=request.user).exists():
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if MedicalAgentOfMedicalInstitution.objects.filter(user=request.user, medical_institution=obj.medical_institution).exists():
            return True
        return False

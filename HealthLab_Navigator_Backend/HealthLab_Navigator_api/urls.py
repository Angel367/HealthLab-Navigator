from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MedicalInstitutionViewSet

router = DefaultRouter()
# Регистрируем ваше представление для модели MedicalInstitution
router.register(r'medical-institution', MedicalInstitutionViewSet, basename='medical-institution')

urlpatterns = [
    path('', include(router.urls))
]

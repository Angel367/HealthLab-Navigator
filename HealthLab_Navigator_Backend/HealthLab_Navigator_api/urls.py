from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
# Регистрируем ваше представление для модели MedicalInstitution
router.register(r'medical-institution', MedicalInstitutionViewSet, basename='medical-institution')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view())
]

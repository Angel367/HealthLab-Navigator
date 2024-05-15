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
router.register(r'medical-service', MedicalServiceViewSet, basename='medical-service')
router.register(r'medical-institution', MedicalInstitutionViewSet, basename='medical-institution')
router.register(r'medical-institution-branch', MedicalInstitutionBranchViewSet, basename='medical-institution-branch')
router.register(r'medical-institution-service', ServiceInMedicalInstitutionViewSet,
                basename='medical-institution-service')
router.register(r'metro-line', MetroLineViewSet, basename='metro-line')
router.register(r'metro-station', MetroStationViewSet, basename='metro-station')
router.register(r'research-material', ResearchMaterialViewSet, basename='research-material')
# router.register(r'illness', IllnessViewSet, basename='illness')
# router.register(r'medical-system', MedicalSystemViewSet, basename='medical-system')
# router.register(r'feedback', FeedbackViewSet, basename='feedback')
# router.register(r'review', ReviewViewSet, basename='review')
# router.register(r'question', ReviewCommentViewSet, basename='review-comment')
# router.register(r'special-offer', SpecialOfferViewSet, basename='special-offer')
# router.register(r'special-offer', SpecialOfferForPatientViewSet, basename='special-offer-for-patient')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view()),
    path('auth/register/', RegisterPatientView.as_view(), name='register-user'),
    path('register/', RegisterAgentView.as_view(), name='register-agent'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path(
        'visiting-service-in-medical-institution/<service_in_medical_institution_id>/',
        get_visiting_service_in_medical_institution,
        name='visiting-service-in-medical-institution'
    ),
    path(
        'visiting-medical-institution/<medical_institution_id>/',
        get_visiting_medical_institution,
        name='visiting-medical-institution'
    ),
    path(
        'visiting-medical-institution-branch/<medical_institution_branch_id>/',
        get_visiting_medical_institution_branch,
        name='visiting-medical-institution-branch'
    ),
]

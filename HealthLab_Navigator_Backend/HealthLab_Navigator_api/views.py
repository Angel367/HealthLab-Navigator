from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .permissions import IsSuperuserOrReadOnly, MedicalAgentPermission

from .serializers import *
from .models import *



class MedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        if (request.user.is_superuser or request.user.is_medical_agent and
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=self.get_object()).exists()):
            return super().update(request, *args, **kwargs)
        else:
            return self.permission_denied(request)


class MedicalInstitutionBranchViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitutionBranch.objects.all()
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]
    serializer_class = MedicalInstitutionBranchSerializer

    def create(self, request, *args, **kwargs):
        medical_institution = MedicalInstitution.objects.get(id=request.data['medical_institution'])
        if (request.user.is_superuser or request.user.is_medical_agent and
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists()):
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        medical_institution = MedicalInstitution.objects.get(id=request.data['medical_institution'])
        if request.user.is_superuser or request.user.is_medical_agent and \
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists():
            return super().update(request, *args, **kwargs)


class MedicalInstitutionServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceInMedicalInstitution.objects.all()
    serializers_class = MedicalInstitutionServiceSerializer
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]

    def create(self, request, *args, **kwargs):
        medical_institution = get_object_or_404(MedicalInstitution.objects.get(id=request.data['medical_institution']))
        if (request.user.is_superuser or request.user.is_medical_agent and
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists()):
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        medical_institution = get_object_or_404(MedicalInstitution.objects.get(id=request.data['medical_institution']))
        if request.user.is_superuser or request.user.is_medical_agent and \
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists():
            return super().update(request, *args, **kwargs)


class MedicalServiceViewSet(viewsets.ModelViewSet):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        elif request.user.is_medical_agent:
            request.data['status'] = 'new'
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            return self.permission_denied(request)


class MedicalInstitutionServicePriceViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]

    def create(self, request, *args, **kwargs):
        medical_service = get_object_or_404(MedicalService.objects.get(id=request.data['medical_service']))
        medical_institution = get_object_or_404(
            MedicalInstitution.objects.get(id=medical_service.medical_institution.id))
        if request.user.is_superuser or request.user.is_medical_agent and \
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists():
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        medical_service = get_object_or_404(MedicalService.objects.get(id=request.data['medical_service']))
        medical_institution = get_object_or_404(
            MedicalInstitution.objects.get(id=medical_service.medical_institution.id))
        if request.user.is_superuser or request.user.is_medical_agent and \
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists():
            return super().update(request, *args, **kwargs)


class IllnessViewSet(viewsets.ModelViewSet):
    queryset = ResearchMedicalIllness.objects.all()
    serializer_class = ResearchMedicalIllnessSerializer
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        elif request.user.is_medical_agent:
            request.data['status'] = 'new'
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            return self.permission_denied(request)


class MedicalSystemViewSet(viewsets.ModelViewSet):
    queryset = ResearchMedicalSystem.objects.all()
    serializer_class = ResearchMedicalSystemSerializer
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.create(request, *args, **kwargs)
        elif request.user.is_medical_agent:
            request.data['status'] = 'new'
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            return self.permission_denied(request)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializerForAll
    permission_classes = []

    def create(self, request, *args, **kwargs):
        if Feedback.objects.filter(email=request.data['email'], text=request.data['text']).exists():
            return Response({'message': 'Feedback already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.serializer_class = FeedbackSerializerModerator
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.serializer_class = FeedbackSerializerModerator
            return super().update(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class ReviewCommentViewSet(viewsets.ModelViewSet):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


class ProfileView(UpdateAPIView, RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class RegisterPatientView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterPatientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            refresh = RefreshToken.for_user(serializer.instance)
            access_token = AccessToken.for_user(serializer.instance)
            res = {
                "refresh": str(refresh),
                "access": str(access_token)
            }
            return Response(
                {
                    'user': serializer.data,
                    'refresh': res['refresh'],
                    'access': res['access']},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAgentView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterAgentSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'user': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialOfferViewSet(viewsets.ModelViewSet):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
    permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]

    def create(self, request, *args, **kwargs):
        medical_institution = get_object_or_404(MedicalInstitution.objects.get(id=request.data['medical_institution']))
        if request.user.is_superuser or request.user.is_medical_agent and \
                MedicalInstitutionAgent.objects.filter(agent=request.user,
                                                       medical_institution=medical_institution).exists():
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            return self.permission_denied(request)


class SpecialOfferForPatientViewSet(viewsets.ModelViewSet):
    queryset = SpecialOfferForPatient.objects.all()
    serializer_class = SpecialOfferForPatientSerializer
    permission_classes = [permissions.IsAuthenticated]



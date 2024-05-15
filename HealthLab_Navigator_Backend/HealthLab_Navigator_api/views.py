from rest_framework import viewsets, permissions, status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .permissions import *
from .models import *
from .serializers import *
from .filters import *


class MedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer
    permission_classes = [MedicalInstitutionPermission]


class MedicalInstitutionBranchViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitutionBranch.objects.all()
    serializer_class = MedicalInstitutionBranchSerializer
    permission_classes = [MedicalInstitutionBranchAndServicePermission]

    def create(self, request, *args, **kwargs):
        if 'medical_institution' not in request.data:
            return Response({"error": "medical_institution is required"}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        if MedicalAgentOfMedicalInstitution.objects.filter(user=request.user, medical_institution_id=request.data['medical_institution']).exists():
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)


class ServiceInMedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = ServiceInMedicalInstitution.objects.all()
    serializer_class = ServiceInMedicalInstitutionSerializer
    permission_classes = [MedicalInstitutionBranchAndServicePermission]

    def create(self, request, *args, **kwargs):
        if 'medical_institution' not in request.data:
            return Response({"error": "medical_institution is required"}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        if MedicalAgentOfMedicalInstitution.objects.filter(user=request.user, medical_institution_id=request.data['medical_institution']).exists():
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)



class MedicalServiceViewSet(viewsets.ModelViewSet):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = MedicalServiceFilter

    # def create(self, request, *args, **kwargs):
    #     if request.user.is_superuser:
    #         return super().create(request, *args, **kwargs)
    #     elif request.user.is_medical_agent:
    #         request.data['status'] = 'new'
    #         return super().create(request, *args, **kwargs)
    #     else:
    #         return self.permission_denied(request)
    #
    # def destroy(self, request, *args, **kwargs):
    #     if request.user.is_superuser:
    #         return super().destroy(request, *args, **kwargs)
    #     else:
    #         return self.permission_denied(request)
    #
    # def update(self, request, *args, **kwargs):
    #     if request.user.is_superuser:
    #         return super().update(request, *args, **kwargs)
    #     else:
    #         return self.permission_denied(request)





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

class MetroLineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetroLine.objects.all()
    serializer_class = MetroLineSerializer
    permission_classes = [permissions.AllowAny]


class MetroStationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetroStation.objects.all()
    serializer_class = MetroStationSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = MetroStationFilter


class ResearchMaterialViewSet(viewsets.ModelViewSet):
    queryset = ResearchMaterial.objects.all()
    serializer_class = ResearchMaterialSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = ResearchMaterialFilter

# class SpecialOfferViewSet(viewsets.ModelViewSet):
#     queryset = SpecialOffer.objects.all()
#     serializer_class = SpecialOfferSerializer
#     permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]
#
#     def create(self, request, *args, **kwargs):
#         medical_institution = get_object_or_404(MedicalInstitution.objects.get(id=request.data['medical_institution']))
#         if request.user.is_superuser or request.user.is_medical_agent and \
#                 MedicalInstitutionAgent.objects.filter(agent=request.user,
#                                                        medical_institution=medical_institution).exists():
#             return super().create(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)

# def destroy(self, request, *args, **kwargs):
#     if request.user.is_superuser:
#         return super().destroy(request, *args, **kwargs)
#     else:
#         return self.permission_denied(request)
#
# def update(self, request, *args, **kwargs):
#     if request.user.is_superuser:
#         return super().update(request, *args, **kwargs)
#     else:
#         return self.permission_denied(request)


# class SpecialOfferForPatientViewSet(viewsets.ModelViewSet):
#     queryset = SpecialOfferForPatient.objects.all()
#     serializer_class = SpecialOfferForPatientSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class IllnessViewSet(viewsets.ModelViewSet):
#     queryset = ResearchMedicalIllness.objects.all()
#     serializer_class = ResearchMedicalIllnessSerializer
#     permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]
#
#     def create(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             return super().create(request, *args, **kwargs)
#         elif request.user.is_medical_agent:
#             request.data['status'] = 'new'
#             return super().create(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)
#
#     def destroy(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             return super().destroy(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)
#
#     def update(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             return super().update(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)
#
#
# class MedicalSystemViewSet(viewsets.ModelViewSet):
#     queryset = ResearchMedicalSystem.objects.all()
#     serializer_class = ResearchMedicalSystemSerializer
#     permission_classes = [IsSuperuserOrReadOnly, MedicalAgentPermission]
#
#     def create(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             return self.create(request, *args, **kwargs)
#         elif request.user.is_medical_agent:
#             request.data['status'] = 'new'
#             return super().create(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)
#
#     def destroy(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             return super().destroy(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)
#
#     def update(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             return super().update(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)


# class FeedbackViewSet(viewsets.ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializerForAll
#     permission_classes = []
#
#     def create(self, request, *args, **kwargs):
#         if Feedback.objects.filter(email=request.data['email'], text=request.data['text']).exists():
#             return Response({'message': 'Feedback already exists'}, status=status.HTTP_400_BAD_REQUEST)
#         return super().create(request, *args, **kwargs)
#
#     def destroy(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             self.serializer_class = FeedbackSerializerModerator
#             return super().destroy(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)
#
#     def update(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             self.serializer_class = FeedbackSerializerModerator
#             return super().update(request, *args, **kwargs)
#         else:
#             return self.permission_denied(request)

# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]  # todo permissions.IsAuthenticated only for create, update, destroy


# class ReviewCommentViewSet(viewsets.ModelViewSet):
#     queryset = ReviewComment.objects.all()
#     serializer_class = ReviewCommentSerializer
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]




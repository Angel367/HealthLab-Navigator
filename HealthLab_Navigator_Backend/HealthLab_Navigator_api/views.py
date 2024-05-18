from django.http import JsonResponse
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .filters import *
from .permissions import *
from .serializers import *


class MedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer
    permission_classes = [MedicalInstitutionPermission]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        add_visit(
            request=request,
            visit_type='medical_institution',
            obj_id=instance.id
        )
        return super().retrieve(request, *args, **kwargs)


class MedicalInstitutionBranchViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitutionBranch.objects.all().order_by('id')
    serializer_class = MedicalInstitutionBranchSerializer
    permission_classes = [MedicalInstitutionBranchAndServicePermission]
    filterset_class = MedicalInstitutionBranchFilter

    def create(self, request, *args, **kwargs):
        if 'medical_institution' not in request.data:
            return Response({"error": "medical_institution is required"}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        if MedicalAgentOfMedicalInstitution.objects.filter(user=request.user, medical_institution_id=request.data[
            'medical_institution']).exists():
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        params = self.request.query_params
        latitude = params.get('latitude')
        longitude = params.get('longitude')

        if latitude and longitude:
            context['user_latitude'] = latitude
            context['user_longitude'] = longitude

        return context

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        add_visit(
            request=request,
            visit_type='medical_institution_branch',
            obj_id=instance.id
        )
        return super().retrieve(request, *args, **kwargs)


class ServiceInMedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = ServiceInMedicalInstitution.objects.all()
    serializer_class = ServiceInMedicalInstitutionSerializer
    permission_classes = [MedicalInstitutionBranchAndServicePermission]
    filterset_class = ServiceInMedicalInstitutionFilter

    def create(self, request, *args, **kwargs):
        if 'medical_institution' not in request.data:
            return Response({"error": "medical_institution is required"}, status=status.HTTP_400_BAD_REQUEST)
        if request.user.is_superuser:
            return super().create(request, *args, **kwargs)
        if MedicalAgentOfMedicalInstitution.objects.filter(user=request.user, medical_institution_id=request.data[
            'medical_institution']).exists():
            return super().create(request, *args, **kwargs)
        else:
            return self.permission_denied(request)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        add_visit(
            request=request,
            visit_type='service_in_medical_institution',
            obj_id=instance.id
        )
        return super().retrieve(request, *args, **kwargs)


class MedicalServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = MedicalServiceFilter


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
    queryset = MetroLine.objects.all().order_by('number')
    serializer_class = MetroLineSerializer
    permission_classes = [permissions.AllowAny]


class MetroStationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetroStation.objects.all().order_by('name')
    serializer_class = MetroStationSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = MetroStationFilter


class ResearchMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResearchMaterial.objects.all()
    serializer_class = ResearchMaterialSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = ResearchMaterialFilter


@api_view(['GET'])
def get_visiting_service_in_medical_institution(request, service_in_medical_institution_id):
    if not ServiceInMedicalInstitution.objects.filter(id=service_in_medical_institution_id).exists():
        return JsonResponse({'error': 'Service in medical institution does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    if not MedicalAgentOfMedicalInstitution.objects.filter(
            user=request.user,
            medical_institution_id=
            ServiceInMedicalInstitution.objects.get(id=service_in_medical_institution_id).medical_institution_id
    ).exists():
        return JsonResponse(
            {'error': 'User is not agent of service of this medical institution'},
            status=status.HTTP_403_FORBIDDEN
        )
    all_visits_of_service_medical_institution = VisitingServiceInMedicalInstitution.objects.filter(
        service_in_medical_institution=service_in_medical_institution_id
    )
    visiting_statistics = get_visiting_statistics_by_visit_data(all_visits_of_service_medical_institution)
    return JsonResponse(visiting_statistics)


@api_view(['GET'])
def get_visiting_medical_institution(request, medical_institution_id):
    if not MedicalInstitution.objects.filter(id=medical_institution_id).exists():
        return JsonResponse({'error': 'Medical institution does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    if not MedicalAgentOfMedicalInstitution.objects.filter(
            user=request.user,
            medical_institution_id=
            MedicalInstitution.objects.get(id=medical_institution_id)
    ).exists():
        return JsonResponse(
            {'error': 'User is not agent of this medical institution'},
            status=status.HTTP_403_FORBIDDEN
        )
    all_visits_of_medical_institution = VisitingMedicalInstitution.objects.filter(
        medical_institution=medical_institution_id
    )
    visiting_statistics = get_visiting_statistics_by_visit_data(all_visits_of_medical_institution)
    return JsonResponse(visiting_statistics)


@api_view(['GET'])
def get_visiting_medical_institution_branch(request, medical_institution_branch_id):
    if not MedicalInstitutionBranch.objects.filter(id=medical_institution_branch_id).exists():
        return JsonResponse({'error': 'Medical institution branch does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    if not MedicalAgentOfMedicalInstitution.objects.filter(
            user=request.user,
            medical_institution_id=
            MedicalInstitutionBranch.objects.get(id=medical_institution_branch_id).medical_institution_id
    ).exists():
        return JsonResponse(
            {'error': 'User is not agent of this medical institution'},
            status=status.HTTP_403_FORBIDDEN
        )
    all_visits_of_medical_institution_branch = VisitingMedicalInstitutionBranch.objects.filter(
        medical_institution_branch=medical_institution_branch_id
    )
    visiting_statistics = get_visiting_statistics_by_visit_data(all_visits_of_medical_institution_branch)
    return JsonResponse(visiting_statistics)


def get_visiting_statistics_by_visit_data(visit_data):
    gender_data_absolute = {
        'unknown': 0,
        'other': 0,
        'male': 0,
        'female': 0
    }
    age_data_absolute = {
        'unknown': 0,
        '0-18': 0,
        '19-30': 0,
        '31-45': 0,
        '46-60': 0,
        '61-75': 0,
        '76+': 0
    }
    total_visits = len(visit_data)
    for visit in visit_data:
        if visit.user is None:
            gender_data_absolute['unknown'] += 1
            age_data_absolute['unknown'] += 1
            continue
        age = visit.user.age
        if age is None:
            age_data_absolute['unknown'] += 1
        else:
            if age < 19:
                age_data_absolute['0-18'] += 1
            elif age < 31:
                age_data_absolute['19-30'] += 1
            elif age < 46:
                age_data_absolute['31-45'] += 1
            elif age < 61:
                age_data_absolute['46-60'] += 1
            elif age < 76:
                age_data_absolute['61-75'] += 1
            else:
                age_data_absolute['76+'] += 1

        gender_data_absolute[visit.user.gender] += 1

    # Calculate percentage
    gender_data_percent = {gender: count / total_visits * 100 if total_visits != 0 else 0 for gender, count in
                           gender_data_absolute.items()}
    age_data_percent = {age_range: count / total_visits * 100 if total_visits != 0 else 0 for age_range, count in
                        age_data_absolute.items()}

    return {
        'gender_data_absolute': gender_data_absolute,
        'age_data_absolute': age_data_absolute,
        'gender_data_percent': gender_data_percent,
        'age_data_percent': age_data_percent
    }


def add_visit(request, visit_type, obj_id):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    if visit_type == 'service_in_medical_institution':
        VisitingServiceInMedicalInstitution.objects.create(
            user=user,
            service_in_medical_institution=ServiceInMedicalInstitution.objects.get(id=obj_id)
        )
    elif visit_type == 'medical_institution':
        VisitingMedicalInstitution.objects.create(
            user=user,
            medical_institution=MedicalInstitution.objects.get(id=obj_id)
        )
    elif visit_type == 'medical_institution_branch':
        VisitingMedicalInstitutionBranch.objects.create(
            user=user,
            medical_institution_branch=MedicalInstitutionBranch.objects.get(id=obj_id)
        )

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

from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MedicalInstitutionSerializer
from .models import MedicalInstitution


class MedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer


# class MedicalInstitutionDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MedicalInstitutionSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         queryset = MedicalInstitution.objects.all()
#         name = self.request.query_params.get('name', None)
#         is_oms_available = self.request.query_params.get('is_oms_available', None)
#
#         if name is not None:
#             queryset = queryset.filter(name__icontains=name)
#
#         if is_oms_available is not None:
#             is_oms_available = is_oms_available.lower() == 'true'
#             queryset = queryset.filter(is_oms_available=is_oms_available)
#
#         return queryset
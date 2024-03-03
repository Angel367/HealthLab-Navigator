from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import rest_framework.permissions
from .permissions import IsSuperuserOrReadOnly

from .serializers import MedicalInstitutionSerializer
from .models import MedicalInstitution


class MedicalInstitutionViewSet(viewsets.ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer
    permission_classes = [IsSuperuserOrReadOnly]

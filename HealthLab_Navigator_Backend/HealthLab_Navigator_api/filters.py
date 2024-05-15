from django_filters import rest_framework as filters
from .models import *


class MedicalServiceFilter(filters.FilterSet):
    exact_name = filters.CharFilter(field_name='name', lookup_expr='exact', label='Точное имя')
    similar_name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='Имя содержит')

    class Meta:
        model = MedicalService
        fields = ['name']


class MetroStationFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = MetroStation
        fields = ['name']


class ResearchMaterialFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = ResearchMaterial
        fields = ['name']


class MedicalInstitutionBranchFilter(filters.FilterSet):
    metro_stations = filters.ModelMultipleChoiceFilter(
        field_name='metro_stations',
        queryset=MetroStation.objects.all()
    )

    class Meta:
        model = MedicalInstitutionBranch
        fields = ['metro_stations']

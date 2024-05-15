from django_filters import rest_framework as filters
from .models import *


class MedicalServiceFilter(filters.FilterSet):
    class Meta:
        model = MedicalService
        fields = {
            'is_active': ['exact'],
            'name': ['icontains'],
            'main_description': ['icontains'],
            'created': ['exact', 'year__gt', 'year__lt'],
            'research_material': ['exact']
        }

    # Дополнительные методы для упорядочивания
    ordering = filters.OrderingFilter(
        # Доступные поля для сортировки
        fields=(
            ('name', 'name'),
        ),
        # По умолчанию сортировка по наименованию (name)
        field_labels={'name': 'Название'}
    )


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

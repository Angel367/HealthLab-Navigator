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


class ServiceInMedicalInstitutionFilter(filters.FilterSet):
    service = filters.ModelMultipleChoiceFilter(
        field_name='service',
        queryset=MedicalService.objects.all(),
    )
    is_active = filters.BooleanFilter()
    medical_institution = filters.ModelMultipleChoiceFilter(
        field_name='medical_institution',
        queryset=MedicalInstitution.objects.all(),
    )
    is_available_oms = filters.BooleanFilter()
    is_available_dms = filters.BooleanFilter()
    is_available_at_home = filters.BooleanFilter()
    is_available_fast_result = filters.BooleanFilter()
    price = filters.RangeFilter()
    price_for_fast_result = filters.RangeFilter()
    price_for_at_home = filters.RangeFilter()
    time_to_complete = filters.DurationFilter()
    time_to_complete_for_fast_result = filters.DurationFilter()

    ordering = filters.OrderingFilter(
        fields=(
            ('service__name', 'service_name'),
            ('is_active', 'is_active'),
            ('medical_institution__name', 'medical_institution_name'),
            ('is_available_oms', 'is_available_oms'),
            ('is_available_dms', 'is_available_dms'),
            ('is_available_at_home', 'is_available_at_home'),
            ('is_available_fast_result', 'is_available_fast_result'),
            ('price', 'price'),
            ('price_for_fast_result', 'price_for_fast_result'),
            ('price_for_at_home', 'price_for_at_home'),
            ('time_to_complete', 'time_to_complete'),
            ('time_to_complete_for_fast_result', 'time_to_complete_for_fast_result'),
            ('internal_code', 'internal_code'),
            ('url', 'url'),
        ),
    )

    class Meta:
        model = ServiceInMedicalInstitution
        fields = ['service', 'is_active', 'medical_institution', 'is_available_oms',
                  'is_available_dms', 'is_available_at_home', 'is_available_fast_result',
                  'price', 'price_for_fast_result', 'price_for_at_home', 'time_to_complete',
                  'time_to_complete_for_fast_result', 'internal_code', 'url', 'ordering']



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

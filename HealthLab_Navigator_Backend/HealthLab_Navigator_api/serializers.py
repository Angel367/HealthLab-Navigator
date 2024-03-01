from rest_framework import serializers
from .models import MedicalInstitution


class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = '__all__'

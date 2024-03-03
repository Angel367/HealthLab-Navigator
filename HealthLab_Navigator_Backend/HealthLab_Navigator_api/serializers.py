from rest_framework import serializers
from .models import *


class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = '__all__'


class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = '__all__'

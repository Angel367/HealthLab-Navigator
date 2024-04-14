from rest_framework import serializers
from .models import *


class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = '__all__'


class MedicalInstitutionBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitutionBranch
        fields = '__all__'


class MedicalInstitutionServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInMedicalInstitution
        fields = '__all__'


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = '__all__'


class ResearchMedicalSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchMedicalSystem
        fields = '__all__'


class ResearchMedicalIllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchMedicalIllness
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'


class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = '__all__'


class SpecialOfferForPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOfferForPatient
        fields = '__all__'


class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class RegisterAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_agent(**validated_data)
        return user

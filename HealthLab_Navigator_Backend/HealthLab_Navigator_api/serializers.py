from geopy.distance import geodesic
from rest_framework import serializers
from .models import *


class MetroLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetroLine
        fields = '__all__'

class MetroStationSerializer(serializers.ModelSerializer):
    line = MetroLineSerializer(read_only=True)
    class Meta:
        model = MetroStation
        fields = '__all__'


class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = '__all__'


class MedicalInstitutionBranchSerializer(serializers.ModelSerializer):
    metro_stations = MetroStationSerializer(many=True, read_only=True)
    distance_to_user = serializers.SerializerMethodField()

    class Meta:
        model = MedicalInstitutionBranch
        fields = '__all__'

    def get_distance_to_user(self, obj):
        if self.context.get('user_latitude') and self.context.get('user_longitude'):
            return get_distance(
                self.context.get('user_latitude'),
                self.context.get('user_longitude'),
                obj.latitude,
                obj.longitude
            )


class ServiceInMedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInMedicalInstitution
        fields = '__all__'





class ResearchMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchMaterial
        fields = '__all__'


class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = '__all__'

class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect')
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        self.validate(validated_data)
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        if not attrs.get('phone_number')[1:].isdigit():
            raise serializers.ValidationError('Phone number must contain only digits')
        if 10 <= len(attrs.get('phone_number')) > 12:
            raise serializers.ValidationError('Phone number must be more or equals 10 and less 12 characters long')
        if CustomUser.objects.filter(phone_number=attrs.get('phone_number')).exists():
            raise serializers.ValidationError('User with this phone number already exists')
        if len(attrs.get('password')) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return attrs


class RegisterAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},

        }

    def create(self, validated_data):
        user = CustomUser.objects.create_agent(**validated_data)
        return user


# class ResearchMedicalSystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResearchMedicalSystem
#         fields = '__all__'
#
#
# class ResearchMedicalIllnessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResearchMedicalIllness
#         fields = '__all__'
#
#
# class FeedbackSerializerForAll(serializers.ModelSerializer):
#     class Meta:
#         model = Feedback
#         fields = ['email', 'text', 'status', 'create', 'id']
#         read_only_fields = ['status', 'create']
#
#
# class FeedbackSerializerModerator(serializers.ModelSerializer):
#     class Meta:
#         model = Feedback
#         fields = '__all__'
#         read_only_fields = ['create']
#
#
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
#
#
# class ReviewCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReviewComment
#         fields = '__all__'
#
#
# class SpecialOfferSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpecialOffer
#         fields = '__all__'
#
#
# class SpecialOfferForPatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpecialOfferForPatient
#         fields = '__all__'


def get_distance(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    distance = geodesic(point1, point2).meters
    return distance

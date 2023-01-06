from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from utils.errors import Errors

User = get_user_model()


class SignUpSerializer(ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    mobile = serializers.CharField(
        required=False,
        # TODO: Add mobile Validator
        validators=[]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'mobile', 'password', 'password2',)
        extra_kwargs = {
            'email': {'required': False},
            'password': {'required': True},
            'password2': {'required': True},
            'mobile': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(Errors.PASSWORD_NOT_MATCH)
        if not attrs.get('mobile') and not attrs.get('email'):
            raise serializers.ValidationError(Errors.NEED_MOBILE_OR_PASSWORD_TO_REGISTER)

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('email'),
            mobile=validated_data.get('mobile'),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


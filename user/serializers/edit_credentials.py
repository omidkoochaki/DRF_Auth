from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from utils.errors import Errors

User = get_user_model()


class EditCredentialsSerializer(ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    mobile = serializers.CharField(
        required=False,
        # TODO: Add mobile Validator
        validators=[]
    )

    password = serializers.CharField(
        write_only=True,
        required=False,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = ('email', 'mobile', 'password', 'password2',)
        extra_kwargs = {
            'email': {'required': False},
            'password': {'required': False},
            'password2': {'required': False},
            'mobile': {'required': False},
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(Errors.PASSWORD_NOT_MATCH)
        if not attrs.get('mobile') and not attrs.get('email') and not attrs.get('password'):
            raise serializers.ValidationError(Errors.NOTHING_FOR_UPDATE)

        return attrs

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        if validated_data.get('email'):
            instance.email = validated_data.get('email')
            instance.is_email_verified = False
        if validated_data.get('mobile'):
            instance.mobile = validated_data.get('mobile')
            instance.is_mobile_verified = False
        instance.save()
        return instance



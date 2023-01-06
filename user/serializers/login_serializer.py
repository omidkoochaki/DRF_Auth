from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from utils.errors import Errors

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginSerializer(ModelSerializer):
    password = serializers.CharField(
        max_length=65,
        write_only=True,
        required=True,
    )
    mobile = serializers.CharField(
        required=False,
        max_length=11
    )
    email = serializers.EmailField(
        required=False,
    )
    # tokens = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['mobile', 'email', 'password']

    def validate(self, attrs):

        if not attrs.get('mobile') and not attrs.get('email'):
            raise serializers.ValidationError(
                Errors.LOGIN_REQUIRES_EMAIL_OR_PHONE
            )

        user = None

        if attrs.get('mobile'):
            try:
                user = User.objects.get(
                    mobile=attrs.get('mobile'),
                    is_mobile_verified=True,
                )
            except:
                # pass the exception for security reasons
                pass
            if user:
                if not user.check_password(attrs.get('password')):
                    user = None

        elif attrs.get('email'):
            try:
                user = User.objects.get(
                    email=attrs.get('email'),
                    is_email_verified=True,
                )
            except:
                pass
            if user:
                if not user.check_password(attrs.get('password')):
                    user = None


        if not user:
            raise AuthenticationFailed(Errors.INVALID_CREDENTIALS)

        return get_tokens_for_user(user)

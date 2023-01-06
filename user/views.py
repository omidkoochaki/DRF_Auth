from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from user.serializers import SignUpSerializer


User = get_user_model()


class SignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = ['post']


class EditCredentials(ModelViewSet):
    pass

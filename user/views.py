from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user.serializers import SignUpSerializer
from user.serializers.edit_credentials import EditCredentialsSerializer

User = get_user_model()


class SignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = ['post']


class EditCredentialsView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    serializer_class = EditCredentialsSerializer
    http_method_names = ['patch']

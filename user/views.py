from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.serializers import SignUpSerializer
from user.serializers.edit_credentials import EditCredentialsSerializer
from user.serializers.login_serializer import LoginSerializer

User = get_user_model()


class SignUpView(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = ['post']


class EditCredentialsView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    serializer_class = EditCredentialsSerializer
    http_method_names = ['patch']


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = LoginSerializer

    queryset = User.objects.all()

    def post(self, request):
        serializer = LoginSerializer(request.data)
        tokens = serializer.validate(request.data)
        return Response(tokens, status=status.HTTP_200_OK)

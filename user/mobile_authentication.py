# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
# from rest_framework_simplejwt.authentication import JWTAuthentication, default_user_authentication_rule
# from rest_framework_simplejwt.tokens import AccessToken
#
# User = get_user_model()
# JWTAuthentication
#
# class MobileAuthBackend(object):
#     """
#     Custom Mobile Backend to perform authentication via mobile
#     """
#
#     def authenticate(self, username=None, password=None):
#         # my_user_model = get_user_model()
#         try:
#             user = User.objects.get(mobile=username)
#             if user.check_password(password):
#                 return user  # return user on valid credentials
#         except User.DoesNotExist:
#             return None  # return None if custom user model does not exist
#         except:
#             return None  # return None in case of other exceptions
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

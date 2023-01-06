from django.contrib import admin

from ..models import (
    User as UserModel,
    ActivationCode as ActivationCodeModel,
    Profile as ProfileModel,
)

from .user import UserAdmin
from .activation_code import ActivationCodeAdmin
from .profile import ProfileAdmin

admin.site.register(UserModel, UserAdmin)
admin.site.register(ActivationCodeModel, ActivationCodeAdmin)
admin.site.register(ProfileModel, ProfileAdmin)

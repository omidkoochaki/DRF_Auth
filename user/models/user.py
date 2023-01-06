from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from utils.base_model import BaseModel
from utils.errors import Errors


class UserManager(BaseUserManager):
    def check_inputs(self, email=None, mobile=None):
        if not email and not mobile:
            raise ValueError(Errors.EMAIL_OR_Mobile_IS_REQUIRED)
        user = self.model()
        if email:
            user = self.model(
                email=self.normalize_email(email),
            )
        if mobile:
            user = self.model(
                mobile=mobile,
            )
        return user

    def create_user(self, email=None, mobile=None, password=None):
        user = self.check_inputs(email=email, mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, mobile=None, password=None):
        user = self.check_inputs(email=email, mobile=mobile)
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, mobile=None, password=None):
        user = self.check_inputs(email=email, mobile=mobile)
        user.set_password(password)
        user.staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        blank=True,
        null=True,
    )
    is_email_verified = models.BooleanField(
        default=False,
        verbose_name='Email Verified',
    )
    mobile = models.CharField(
        unique=True,
        verbose_name='Mobile',
        blank=True,
        null=True,
    )
    is_mobile_verified = models.BooleanField(
        default=False,
        verbose_name='Mobile Verified',
    )

    def get_username_field(self):
        if self.email:
            return 'email'
        elif self.mobile:
            return 'mobile'

    USERNAME_FIELD = get_username_field()

    objects = UserManager()

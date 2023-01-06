from django.contrib.auth import get_user_model
from django.db import models

from utils.base_model import BaseModel

User = get_user_model()


class Profile(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        unique=True,
    )
    bio = models.CharField(
        max_length=128,
        default='',
        blank=True,
        null=True,
        verbose_name='Bio',
    )
    display_name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        default='new user',
        verbose_name='Display Name'
    )

    def __str__(self):
        return self.user.__str__()

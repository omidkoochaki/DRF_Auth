from django.contrib.auth import get_user_model
from django.db import models

from utils.base_model import BaseModel

User = get_user_model()


class ActivationCode(BaseModel):

    TYPE_CHOICES = (
        ('REGISTER', 'REGISTER'),
        ('FORGET', 'FORGET'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activation_codes',
    )
    code = models.CharField(
        max_length=16,
        verbose_name='Code',
    )
    type = models.CharField(
        max_length=128,
        choices=TYPE_CHOICES,
        verbose_name='Type',
        default='REGISTER'
    )

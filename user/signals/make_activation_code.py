from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import ActivationCode
from utils.functions import generate_random_code

User = get_user_model()


@receiver(signal=post_save, sender=User)
def make_activation_code(sender, instance, created, **kwargs):
    if ((instance.mobile and not instance.is_mobile_verified) or (instance.email and not instance.is_email_verified))\
            and instance.password:

        activation_code = ActivationCode(
            user=instance,
            code=generate_random_code(1000, 9999),
            type='REGISTER'
        )
        activation_code.save()

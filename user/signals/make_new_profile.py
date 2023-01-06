from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User, Profile, ActivationCode
from utils.functions import generate_random_code


@receiver(signal=post_save, sender=User)
def make_new_profile(sender, instance, created, **kwargs):
    new_profile = Profile(
        user=instance
    )
    new_profile.save()
    if instance.mobile:
        activation_code = ActivationCode(
            user=instance,
            code=generate_random_code(1000, 9999),
            type='REGISTER'
        )
        activation_code.save()

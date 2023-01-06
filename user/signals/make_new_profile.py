from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.tasks import send_otp
from user.models import Profile, ActivationCode
from utils.functions import generate_random_code

User = get_user_model()


@receiver(signal=post_save, sender=User)
def make_new_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )

